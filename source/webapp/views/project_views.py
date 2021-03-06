from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from webapp.forms import ProjectForm, SimpleSearchForm
from webapp.models import Project


class ProjectIndexView(ListView):
    template_name = 'project/index.html'
    model = Project
    context_object_name = 'projects'

    # def get_queryset(self):
    #     return Project.objects.all().order_by('created_at')


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
            queryset = queryset.filter(Q(name__icontains=self.query))
        return queryset


class ProjectView(TemplateView):
    template_name = 'project/project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_pk = kwargs.get('pk')
        context['project'] = get_object_or_404(Project, pk=project_pk)
        return context



class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'project/create.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})



class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})



class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'project/delete.html'
    model = Project
    context_key = 'project'
    success_url = reverse_lazy('webapp:project_index')
