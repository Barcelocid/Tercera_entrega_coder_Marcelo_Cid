from django.urls import path
from . import views

urlpatterns = [
    path('agregar_comida/', views.agregar_comida, name='agregar_comida'), # Visualizacion template "agregar_comida"
    path('agregar_pais/', views.agregar_pais, name='agregar_pais'), # Visualizacion template "agregar_pais"
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'), # Visualizacion template "agregar_cliente"
]
