from django.shortcuts import render
from .models import Veiculo

def home(request):
    return render (request, 'home.html')

def lista_carros(request):
    carros = Veiculo.objects.all()
    return render (request, 'lista_carros.html', {'carros': carros})

def detalhe_carro(request, id):
    carro = Veiculo.objects.get(id=id)
    return render (request, 'detalhe_carro.html',{'carro': carro})

def sobre(request):
    return render (request, 'sobre.html')