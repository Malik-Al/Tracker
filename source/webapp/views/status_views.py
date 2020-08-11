from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.forms import StatusForm
from webapp.models import Status




class StatusIndexView(ListView):
    template_name = 'status/status_index.html'
    model = Status
    context_object_name = 'statuses'



class StatusCreateView(LoginRequiredMixin, CreateView):
    template_name = 'status/status_create.html'
    form_class = StatusForm
    model = Status

    def get_success_url(self):
        return reverse('status_index')




class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    template_name = 'status/status_update.html'
    form_class = StatusForm
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('status_index')




class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'status/status_delete.html'
    form_class = StatusForm
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('status_index')