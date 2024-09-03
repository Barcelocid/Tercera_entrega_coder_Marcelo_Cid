from django.shortcuts import render, redirect
from .forms import PaisForm, ClienteForm, ComidaForm

def agregar_pais(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_pais')  # Redirige a la vista combinada después de guardar
    else:
        form = PaisForm()
    return render(request, 'agregar_pais.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            return redirect('agregar_cliente')  # Redirige de vuelta al formulario para agregar otro cliente
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})


def agregar_comida(request):
    if request.method == 'POST':
        form = ComidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_comida')  # Redirige a la vista combinada después de guardar
    else:
        form = PaisForm()
    return render(request, 'agregar_comida.html', {'form': form})


