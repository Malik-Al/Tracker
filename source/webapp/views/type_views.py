from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView
from webapp.forms import TypeForm
from webapp.models import Type
from .base_views import UpdateView, DeleteView




class TypeIndexView(ListView):
    template_name = 'type/index.html'
    model = Type
    context_object_name = 'types'



class TypeCreateView(CreateView):
    template_name = 'type/create.html'
    form_class = TypeForm
    model = Type

    def get_success_url(self):
        return reverse('type_index')



class TypeUpdateView(UpdateView):
    template_name = 'type/update.html'
    form_class = TypeForm
    model = Type
    context_key = 'type'

    def get_redirect_url(self):
        return reverse('type_index')



class TypeDeleteView(DeleteView):
    template_name = 'type/delete.html'
    model = Type
    context_key = 'type'
    redirect_url = reverse_lazy('type_index')






