from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from webapp.forms import StatusForm
from webapp.models import Status


class StatusIndexView(ListView):
    template_name = 'status/status_index.html'
    model = Status
    context_object_name = 'statuses'



class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
            form = StatusForm()
            return render(request, 'status/status_create.html', context={'form': form})
    def post(self, request, *args, **kwargs):
            form = StatusForm(data=request.POST)
            if form.is_valid():
                Status.objects.create(
                    name=form.cleaned_data['status'],

                )
                return redirect('status_index')
            else:
                return render(request, 'status/status_create.html', context={'form': form})




class StatusUpdateView(View):
    def get(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        form = StatusForm(data={
            'status': status.name,


        })
        return render(request, 'status/status_update.html', context={'form': form, 'status': status})

    def post(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status.name = form.cleaned_data['status']
            status.save()
            return redirect('status_index')
        else:
            return render(request, 'status/status_update.html', context={'form': form, 'status': status})


class StatusDeleteView(View):
    def get(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        return render(request, 'status/status_delete.html', context={'status': status})
    def post(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        status.delete()
        return redirect('status_index')



