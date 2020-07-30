from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView
from webapp.forms import StatusForm
from webapp.models import Status
from .base_views import UpdateView, DeleteView




class StatusIndexView(ListView):
    template_name = 'status/status_index.html'
    model = Status
    context_object_name = 'statuses'



class StatusCreateView(CreateView):
    template_name = 'status/status_create.html'
    form_class = StatusForm
    model = Status

    def get_success_url(self):
        return reverse('status_index')



class StatusUpdateView(UpdateView):
    template_name = 'status/status_update.html'
    form_class = StatusForm
    model = Status
    context_key = 'status'

    def get_redirect_url(self):
        return reverse('status_index')



class StatusDeleteView(DeleteView):
    template_name = 'status/status_delete.html'
    context_key = 'status'
    model = Status
    redirect_url = reverse_lazy('status_index')
