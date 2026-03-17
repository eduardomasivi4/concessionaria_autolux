from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carros/', views.lista_carros, name='carros'),
    path('detalhe_carro/<int:id>/', views.detalhe_carro, name='detalhe_carro'),
    
]
