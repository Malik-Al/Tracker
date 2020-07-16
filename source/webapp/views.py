from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from webapp.models import Task

#
# def index_view(request, *args, **kwargs):
#     task = Task.objects.all()
#     return render(request, 'index.html', context={
#         'task': task
#
#     })


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'tasks': Task.objects.all()}



class TaskView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_pk = kwargs.get('pk')
        context['task'] = get_object_or_404(Task, pk=task_pk)
        return context

