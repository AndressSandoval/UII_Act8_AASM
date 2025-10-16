from django.shortcuts import render, redirect, get_object_or_404
from .models import Inventario


# Listar inventario
def index(request):
    inventarios = Inventario.objects.all()
    # Templates are stored under app_inventario/templates/app_inventario/
    return render(request, 'app_inventario/listar_inventario.html', {'inventarios': inventarios})


def ver_inventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    return render(request, 'app_inventario/ver_inventario.html', {'inventario': inventario})


def agregar_inventario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        anio = request.POST.get('anio')
        fecha = request.POST.get('fecha')
        disponible = request.POST.get('disponible')
        Inventario.objects.create(nombre=nombre, anio=anio, fecha=fecha, disponible=disponible)
        return redirect('inicio')
    return render(request, 'app_inventario/agregar_inventario.html')


def editar_inventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    if request.method == 'POST':
        inventario.nombre = request.POST.get('nombre')
        inventario.anio = request.POST.get('anio')
        inventario.fecha = request.POST.get('fecha')
        inventario.disponible = request.POST.get('disponible')
        inventario.save()
        return redirect('inicio')
    return render(request, 'app_inventario/editar_inventario.html', {'inventario': inventario})


def borrar_inventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    if request.method == 'POST':
        inventario.delete()
        return redirect('inicio')
    return render(request, 'app_inventario/borrar_inventario.html', {'inventario': inventario})