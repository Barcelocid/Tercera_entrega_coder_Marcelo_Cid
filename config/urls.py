'''
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
#from django.template import Context, Template
from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', views.saludo), #Agregamos esta linea
    path('segunda-vista/', views.segunda_vista), #Agregamos esta linea
    path('nombre/<nombre>/<apellido>/', views.nombre), #Agregamos esta linea
    path('miTemplate/', views.probando_template),
    path('miTemplate2/', views.probando_templates2),
]
'''
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),  # Incluye las URLs de la aplicación clientes
]

