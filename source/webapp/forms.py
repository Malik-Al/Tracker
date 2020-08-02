from django import forms
from webapp.models import Status, Type, Task, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = []


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        exclude = []


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        exclude = []


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = []