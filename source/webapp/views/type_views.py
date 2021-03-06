from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.forms import TypeForm
from webapp.models import Type




class TypeIndexView(ListView):
    template_name = 'type/index.html'
    model = Type
    context_object_name = 'types'



class TypeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'type/create.html'
    form_class = TypeForm
    model = Type

    def get_success_url(self):
        return reverse('webapp:type_index')




class TypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Type
    template_name = 'type/update.html'
    form_class = TypeForm
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('webapp:type_index')




class TypeDeleteView(LoginRequiredMixin, DeleteView):
    model = Type
    template_name = 'type/delete.html'
    form_class = TypeForm
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('webapp:type_index')


