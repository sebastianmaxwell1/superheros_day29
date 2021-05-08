from django.shortcuts import render
from django.http import HttpResponse
from .models import Superhero


def index(request):
    all_superheros = Superhero.objects.all()
    context = {
        'all_superheros': all_superheros
    }
    return render(request, 'superheros/index.html', context)


def detail(request, superhero_id):
    pick_superhero = Superhero.objects.get(Superhero, pk=superhero_id)
    context = {
        'pick_superhero': pick_superhero
    }
    return render(request, 'superheros/detail.html', context)


def create(request, superhero_id):
    form = SuperherForm(request.POST or None, request.FILES or None)

    context = {
        'form': form
    }

    if form.is_valid():
        form.save()
        return redirect('superheros:index')
    else:
        return render(request, 'superheros/create.html', context)


def edit(request, superhero_id):
    superhero = get_objects_or_404(Superhero, pk=superhero_id)

    form = SuperheroForm(request.POST or None, request.FILES or None, instance=superhero)

    if form.is_valid():
        form.save()
        return redirect('superheros:index')

    context = {
        'form': form,
        'superhero image': superhero
    }

    return render(request, 'superheros/edit.html', context)


def delete(request, superhero_id):
    superhero = get_objects_or_404(Superhero, pk=superhero_id)
    if request.method == 'POST':
        superhero.delete()
        return redirect('superheros:index')

    context = {
        'superhero': superhero
    }

    return render(request, 'superheros/delete.html', context)
