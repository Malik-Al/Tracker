from django.shortcuts import render
from django.views.generic import TemplateView

from webapp.models import Task


def index_view(request, *args, **kwargs):
    task = Task.objects.all()
    return render(request, 'index.html', context={
        'task': task

    })