from django.shortcuts import render
from .models import Veiculo

def home(request):
    return render (request, 'home.html')

def lista_carros(request):
    carros = Veiculo.objects.all()
    return render (request, 'lista_carros.html', {'veiculo': carros})

def detalhe_carro(request):
    return render (request, 'detalhe_carro.html')