from django.shortcuts import render, redirect, get_object_or_404
from .models import Casa
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CasaForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.


def index(request):
    return render(request, 'inmoss/index.html')

def servicios(request):
    casas=Casa.objects.all()
    context={"casas": casas}
    return render(request, 'inmoss/servicios.html', context)

@login_required
def servicios(request):
    casas=Casa.objects.all()
    context={"casas": casas}
    return render(request, 'inmoss/servicios.html', context)

@login_required
def menu(request):
    request.session["usuario"]="cgarcia"
    usuario=request.session["usuario"]
    context={'usuario':usuario}
    return render(request, 'inmoss/index.html', context)


def detalle_casa(request, casa_id):
    casa = get_object_or_404(Casa, id_casa=casa_id)
    return render(request, 'inmoss/detalle_casa.html', {'casa': casa})

def logoutt(request):
    logout(request)
    return render(request, 'inmoss/index.html')



def pago(request, id_casa):
    casa = get_object_or_404(Casa, id_casa=id_casa)
    context = {
        'casa': casa
    }
    return render(request, 'inmoss/pago.html', context)


def casa_delete(request, id_casa):
    casa = get_object_or_404(Casa, id_casa=id_casa)
    casa.delete()
    # Redirecciona a la página de servicios después de eliminar la casa
    return redirect('servicios')

def proceso_pago(request, id_casa):
    casa = get_object_or_404(Casa, id_casa=id_casa)

    if request.method == 'POST':
        # Procesar el formulario de pago aquí
        # Suponiendo que recibimos los datos del formulario (rut, nombre, apellido, tarjeta, ccv, etc.)
        # y se validan correctamente

        # Actualizar el estado de la casa a no disponible
        casa.disponibilidad = 'no_disponible'
        casa.save()

        # Redirigir a alguna página de confirmación o a otra vista
        return redirect('index')

    context = {
        'casa': casa
    }
    return render(request, 'inmoss/proceso_pago.html', context)


def listar_casas(request):
    casas = Casa.objects.all()
    return render(request, 'listar_casas.html', {'casas': casas})


def casa_add(request):
    if request.method == 'POST':
        form = CasaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicios')
    else:
        form = CasaForm()
    return render(request, 'inmoss/casa_add.html', {'form': form})



def casa_edit(request, casa_id):
    casa = get_object_or_404(Casa, id_casa=casa_id)
    if request.method == 'POST':
        form = CasaForm(request.POST, instance=casa)
        if form.is_valid():
            form.save()
            return redirect('servicios')
    else:
        form = CasaForm(instance=casa)
    return render(request, 'inmoss/casa_edit.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}!')
            return redirect('login')  # Redirige al login después del registro
    else:
        form = UserRegisterForm()
    return render(request, 'inmoss/register.html', {'form': form})


def crear_casa(request):
    if request.method == 'POST':
        form = CasaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_casas')
    else:
        form = CasaForm()
    return render(request, 'crear_casa.html', {'form': form})

def editar_casa(request, id):
    casa = get_object_or_404(Casa, id=id)
    if request.method == 'POST':
        form = CasaForm(request.POST, request.FILES, instance=casa)
        if form.is_valid():
            form.save()
            return redirect('listar_casas')
    else:
        form = CasaForm(instance=casa)
    return render(request, 'editar_casa.html', {'form': form})

def eliminar_casa(request, id):
    casa = get_object_or_404(Casa, id=id)
    if request.method == 'POST':
        casa.delete()
        return redirect('listar_casas')
    return render(request, 'eliminar_casa.html', {'casa': casa})
