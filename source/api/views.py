from django.shortcuts import render
from rest_framework import viewsets
from webapp.models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
   queryset = Project.objects.all()
   serializer_class = ProjectSerializer

