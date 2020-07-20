from django import forms
from django.forms import widgets
from webapp.models import Status, Type


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Заголовок')
    description = forms.CharField(max_length=3000, required=True, label='Текст', widget=widgets.Textarea)

    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False, label='Status', empty_label=None)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False, label='Type', empty_label=None)



class StatusForm(forms.Form):
    status = forms.CharField(max_length=30, required=True, label='Status')


class TypeForm(forms.Form):
    type = forms.CharField(max_length=30, required=True, label='Type')