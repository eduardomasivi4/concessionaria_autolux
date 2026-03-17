from django.shortcuts import render
from .models import Veiculo

def home(request):
    return render (request, 'home.html')

def carros(request):
    return render (request, 'carros.html')