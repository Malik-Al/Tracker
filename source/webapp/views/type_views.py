from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.forms import TypeForm
from webapp.models import Type




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
    model = Type
    template_name = 'type/update.html'
    form_class = TypeForm
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('type_index')




class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'type/delete.html'
    form_class = TypeForm
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('type_index')


