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
    chose_superhero = Superhero.objects.get(pk=superhero_id)
    return render(request, 'superheros/index.html', chose_superhero)
