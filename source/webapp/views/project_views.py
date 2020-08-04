from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectIndexView(ListView):
    template_name = 'project/index.html'
    model = Project
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.all().order_by('created_at')





class ProjectView(TemplateView):
    template_name = 'project/project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_pk = kwargs.get('pk')
        context['project'] = get_object_or_404(Project, pk=project_pk)
        return context



class ProjectCreateView(CreateView):
    template_name = 'project/create.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})



class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})



class ProjectDeleteView(DeleteView):
    template_name = 'project/delete.html'
    model = Project
    context_key = 'project'
    success_url = reverse_lazy('project_index')
