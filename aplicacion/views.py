from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def cortes(request):
    ctx = {"cortes": Corte.objects.all() }
    return render(request, "aplicacion/cortes.html",ctx)

def peindados(request):
    ctx = {"peinados": Peinado.objects.all() }
    return render(request, "aplicacion/peinados.html",ctx)

def estilistas(request):
    ctx = {"estilistas": Estilista.objects.all() }
    return render(request, "aplicacion/estilistas.html", ctx)


def corteForm(request):
    if request.method == 'POST':
        form = CorteForm(request.POST)
        if form.is_valid():
            
            corte_nombre = form.cleaned_data['nombre']
            corte_descripcion = form.cleaned_data['descripcion']
            corte_precio = form.cleaned_data['precio']
            corte_duracion_minutos = form.cleaned_data['duracion_minutos']
            corte = Corte(nombre= corte_nombre, descripcion =corte_descripcion,precio=corte_precio,
                          duracion_minutos= corte_duracion_minutos )
            corte.save()
            return render(request, 'aplicacion/base.html', {"form":form})  
        
    else:
        form = CorteForm()

    return render(request, 'aplicacion/corteForm.html', {'form': form})


def peinadoForm(request):
    if request.method == 'POST':
        form = PeinadoForm(request.POST)
        if form.is_valid():
            
            peinado_nombre = form.cleaned_data['nombre']
            peinado_descripcion = form.cleaned_data['descripcion']
            peinado_precio = form.cleaned_data['precio']
            peinado_duracion_minutos = form.cleaned_data['duracion_minutos']
            peinado = Peinado(nombre= peinado_nombre, descripcion = peinado_descripcion, precio=peinado_precio,
                          duracion_minutos= peinado_duracion_minutos )
            peinado.save()
            return render(request, 'aplicacion/base.html', {"form":form})  
    else:
        form = PeinadoForm()

    return render(request, 'aplicacion/peinadoForm.html', {'form': form})

def estilistaForm(request):
    if request.method == 'POST':
        form = EstilistaForm(request.POST)
        if form.is_valid():
            
            estilista_nombre = form.cleaned_data['nombre']
            estilista_telefono = form.cleaned_data['telefono']
            estilista_email = form.cleaned_data['email']
            estilista_especialidad = form.cleaned_data['especialidad']
            estilista_experiencia_anios = form.cleaned_data['experiencia_anios']
            estilista = Estilista(nombre= estilista_nombre, telefono = estilista_telefono, email= estilista_email,
                          especialidad= estilista_especialidad, experiencia_anios =estilista_experiencia_anios )
            estilista.save()
            return render(request, 'aplicacion/base.html', {"form":form})   
    else:
        form = EstilistaForm()

    return render(request, 'aplicacion/estilistaForm.html', {'form': form})

def buscarCorte(request):
    return render(request, "aplicacion/buscarCorte.html")

def buscar_corte(request):
    if request.GET.get('precio'):
        precio = request.GET.get('precio')
        cortes = Corte.objects.filter(precio__icontains=precio)
        print(Corte)
        return render(request, 
                      "aplicacion/resultadosCortes.html", 
                      {"precio": precio , "cortes": cortes})
    return HttpResponse("No se ingresaron datos para buscar!")

def buscarPeinado(request):
    return render(request, "aplicacion/buscarPeinado.html")

def buscar_peinado(request):
    if request.GET.get('nombre'):
        nombre = request.GET.get('nombre')
        peinados = Peinado.objects.filter(nombre__icontains=nombre)
        print(Peinado)
        return render(request, 
                      "aplicacion/resultadosPeinados.html", 
                      {"Nombre": nombre , "peinados": peinados})
    return HttpResponse("No se ingresaron datos para buscar!")

def buscarEstilista(request):
    return render(request, "aplicacion/buscarEstilista.html")

def buscar_estilista(request):
    if request.GET.get('nombre'):
        nombre = request.GET.get('nombre')
        estilista = Estilista.objects.filter(nombre__icontains=nombre)
        print(Estilista)
        return render(request, 
                      "aplicacion/resultadosEstilistas.html", 
                      {"Nombre": nombre , "estilistas": estilista})
    return HttpResponse("No se ingresaron datos para buscar!")


