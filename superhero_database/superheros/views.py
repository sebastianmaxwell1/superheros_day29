from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Superhero
from django.forms import ModelForm


class SuperheroForm(ModelForm):
    class Meta:
        model = Superhero
        fields = ['name', 'alter_ego', 'ability', 'secondary_superhero_ability', 'catchphrase']


def index(request):
    all_superheros = Superhero.objects.all()
    context = {
        'all_superheros': all_superheros
    }
    return render(request, 'superheros/index.html', context)


def detail(request, superhero_id):
    pick_superhero = get_object_or_404(Superhero, pk=superhero_id)
    context = {
        'pick_superhero': pick_superhero
    }
    return render(request, 'superheros/detail.html', context)


def create(request):
    form = SuperheroForm(request.POST or None, request.FILES or None)

    context = {
        'form': form
    }

    if form.is_valid():
        form.save()
        return redirect('superheros:index')

    else:
        return render(request, 'superheros/create.html', context)


def edit(request, superhero_id):
    # superhero = get_object_or_404(Superhero, pk=superhero_id)

    form = SuperheroForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('superheros:index')

    context = {
        'form': form

    }

    return render(request, 'superheros/edit.html', context)


def delete(request, superhero_id):
    superhero = get_object_or_404(Superhero, pk=superhero_id)
    if request.method == 'POST':
        superhero.delete()
        return redirect('superheros:index')

    context = {
        'superhero': superhero
    }

    return render(request, 'superheros/delete.html', context)

