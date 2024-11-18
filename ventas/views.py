from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto

# Create your views here.

def index(request):
    return render(request, 'ventas/index.html')


def carrito(request):
    carrito_ids = request.session.get('carrito', [])
    productos_carrito = Producto.objects.filter(id_producto__in=carrito_ids)
    context = {
        'productos_carrito': productos_carrito
    }
    return render(request, 'ventas/carrito.html', context)


def delete_producto(request, id_producto):
    carrito = request.session.get('carrito', [])
    
    if id_producto in carrito:
        carrito.remove(id_producto)
        
    request.session['carrito'] = carrito
    return redirect('carrito')


def ofertas(request):
    productos = Producto.objects.all()
    context = {"productos":productos}
    return render(request, 'ventas/ofertas.html', context)


def producto_seleccionado(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    carrito = request.session.get('carrito', [])
    
    if producto.id_producto not in carrito:
        carrito.append(producto.id_producto)
        
    request.session['carrito'] = carrito
    
    messages.success(request, f'El producto {producto.nombre_prod} ha sido agregado al carrito.')
    return redirect('ofertas')