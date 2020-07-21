from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from webapp.forms import TypeForm
from webapp.models import Type


class TypeIndexView(ListView):
    template_name = 'type/index.html'
    model = Type
    context_object_name = 'types'




class TypeCreateView(View):
    def get(self, request, *args, **kwargs):
            form = TypeForm()
            return render(request, 'type/create.html', context={'form': form})
    def post(self, request, *args, **kwargs):
            form = TypeForm(data=request.POST)
            if form.is_valid():
                Type.objects.create(
                    name=form.cleaned_data['type'],

                )
                return redirect('type_index')
            else:
                return render(request, 'type/create.html', context={'form': form})




class TypeUpdateView(View):
    def get(self, request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        form = TypeForm(data={
            'type': type.name,


        })
        return render(request, 'type/update.html', context={'form': form, 'type': type})

    def post(self, request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type.name = form.cleaned_data['type']
            type.save()
            return redirect('type_index')
        else:
            return render(request, 'type/update.html', context={'form': form, 'type': type})


class TypeDeleteView(View):
    def get(self, request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        return render(request, 'type/delete.html', context={'type': type})
    def post(self, request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        type.delete()
        return redirect('type_index')







