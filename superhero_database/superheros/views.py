from django.shortcuts import render
from django.http import HttpResponse
from .models import Superhero
# from .urls import detail
# Create your views here.


def index(request):
    all_superheros = Superhero.objects.all()
    context = {
        'all_superheros': all_superheros
    }
    return render(request, 'superheros/index.html', context)

# def detail(request, superhero_id)