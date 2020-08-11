from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import  get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from webapp.forms import TaskForm, SimpleSearchForm
from webapp.models import Task



class IndexView(ListView):
    template_name = 'task/index.html'
    model = Task
    context_object_name = 'tasks'
    paginate_by = 1
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        form = SimpleSearchForm(self.request.GET)
        query = None
        if form.is_valid():
            query = form.cleaned_data['search']
        self.form = form
        self.query = query
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if self.query:
            context['query'] = urlencode({'search': self.query})
        context['form'] = self.form
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.query:
            queryset = queryset.filter(Q(summary__icontains=self.query) | Q(description__icontains=self.query))
        return queryset



class TaskView(TemplateView):
    template_name = 'task/task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_pk = kwargs.get('pk')
        context['task'] = get_object_or_404(Task, pk=task_pk)
        return context




class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'task/create.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})




class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task/update.html'
    form_class = TaskForm
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})



class TaskDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'task/delete.html'
    model = Task
    context_key = 'task'
    success_url = reverse_lazy('index')

