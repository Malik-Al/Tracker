from django.shortcuts import  get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from webapp.forms import TaskForm
from webapp.models import Task
from .base_views import UpdateView, DeleteView



class IndexView(ListView):
    template_name = 'task/index.html'
    model = Task
    context_object_name = 'tasks'
    paginate_by = 1
    paginate_orphans = 1



class TaskView(TemplateView):
    template_name = 'task/task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_pk = kwargs.get('pk')
        context['task'] = get_object_or_404(Task, pk=task_pk)
        return context


class TaskCreateView(CreateView):
    template_name = 'task/create.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})



class TaskUpdateView(UpdateView):
    template_name = 'task/update.html'
    form_class = TaskForm
    model = Task
    context_key = 'task'

    def get_redirect_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})



class TaskDeleteView(DeleteView):
    template_name = 'task/delete.html'
    context_key = 'task'
    model = Task
    redirect_url = reverse_lazy('index')







