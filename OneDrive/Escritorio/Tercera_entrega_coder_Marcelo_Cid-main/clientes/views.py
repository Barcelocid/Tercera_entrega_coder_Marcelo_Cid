from django.shortcuts import render, redirect
from .forms import PaisForm, ClienteForm, ComidaForm # Importar los forms
from .models import cliente, pais, comida  # Importar los modelos correspondientes
from django.db.models import Q  # Importar Q para realizar las busquedas

def home(request):
    query = request.GET.get('q')  # Obtener el valor buscado
    clientes = []
    paises = []
    comidas = []

    # Si se ha enviado una búsqueda, filtra los resultados
    if query:
        # Buscar en el modelo Cliente (en nombre y apellido)
        clientes = cliente.objects.filter(
            Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(rut__icontains=query)
        )
        
        # Buscar en el modelo Pais (en el nombre del país y de la ciudad)
        paises = pais.objects.filter(
            Q(pais__icontains=query) | Q(ciudad__icontains=query)
        )

        # Buscar en el modelo Comida (en fondo, bebida y postre)
        comidas = comida.objects.filter(
            Q(fondo__icontains=query) | Q(bebida__icontains=query) | Q(postre__icontains=query)
        )

    context = {
        'query': query,
        'clientes': clientes,
        'paises': paises,
        'comidas': comidas,
    }

    return render(request, 'home.html', context)




    

def agregar_pais(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la vista combinada después de guardar
    else:
        form = PaisForm()
    return render(request, 'agregar_pais.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            return redirect('home')  # Redirige de vuelta al formulario para agregar otro cliente
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})


def agregar_comida(request):
    if request.method == 'POST':
        form = ComidaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos del formulario en la base de datos
            return redirect('home')  # Redirige al inicio o a otra página tras guardar
    else:
        form = ComidaForm()  # Crea un formulario vacío en solicitudes GET

    return render(request, 'agregar_comida.html', {'form': form})


