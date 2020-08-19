from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView
from accounts.forms import UserCreationForm, UserChangeForm, UserChangePasswordForm


def register_view(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
    elif request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                first_name= form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('webapp:index')
        else:
            return render(request, 'register.html', {'form': form})


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'


class UserChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_update.html'
    form_class = UserChangeForm
    context_object_name = 'user_obj'

    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})


class UserChangePasswordView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_password_change.html'
    form_class = UserChangePasswordForm
    context_object_name = 'user_obj'

    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})




class UserListView(ListView):
    template_name = 'user_list.html'
    model = User
    context_object_name = 'user_obj'

