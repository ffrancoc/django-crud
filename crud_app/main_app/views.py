from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto

def index(request):
    productos = Producto.objects.all()

    context={
        'productos': productos
    }        
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        nombre = request.POST['txtnombre']
        cantidad = request.POST['txtcantidad']
        precio = request.POST['txtprecio']
        
        try:
            Producto.objects.create(nombre=nombre, cantidad=cantidad, precio=precio)
            messages.success(request, "Registro creado exitosamente", extra_tags="correcto")
        except Exception as ex:
            messages.success(request, "Error al guardar el registro", extra_tags="incorrecto")
        
    return redirect('index')


def update(request):
    if request.method == 'POST':
        id = request.POST['txtid']
        nombre = request.POST['txtnombre']
        cantidad = request.POST['txtcantidad']
        precio = request.POST['txtprecio']
        
        try:
            producto = Producto.objects.get(id=id)
            producto.nombre = nombre
            producto.cantidad = cantidad
            producto.precio = precio    
            producto.save()        
            messages.success(request, "Registro actualizado exitosamente", extra_tags="correcto")
        except Exception as ex:
            messages.success(request, "Error al actualizar el registro", extra_tags="incorrecto")
        
    return redirect('index')


def delete(request, id):
    if request.method == 'GET':        
        try:
            producto = Producto.objects.get(id=id)
            producto.delete()
            messages.success(request, "Registro eliminado exitosamente", extra_tags="correcto")
        except Exception as ex:
            messages.success(request, "Error al eliminar el registro", extra_tags="incorrecto")
        
    return redirect('index')
    