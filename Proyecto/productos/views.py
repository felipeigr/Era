from django.shortcuts import render
from .models import Producto

def index(request):
    productos_list = Producto.objects.all() 
    context = {"productos": productos_list}  
    return render(request, 'productos/index.html', context)

def valo(request):
    productos = Producto.objects.all()  # Reutilizamos la lógica para obtener los productos
    context = {'productos': productos}
    return render(request, 'productos/valo.html', context)


def lol(request):
    productos = Producto.objects.all()  # Reutilizamos la lógica para obtener los productos
    context = {'productos': productos}
    return render(request, 'productos/lol.html', context)


def login(request):
    productos = Producto.objects.all()  # Reutilizamos la lógica para obtener los productos
    context = {'productos': productos}
    return render(request, 'productos/login.html', context)


def nosotros(request):
    productos = Producto.objects.all()  # Reutilizamos la lógica para obtener los productos
    context = {'productos': productos}
    return render(request, 'productos/nosotros.html', context)


def rp(request):
    productos = Producto.objects.all()  # Reutilizamos la lógica para obtener los productos
    context = {'productos': productos}
    return render(request, 'productos/rp.html', context)


def carrito(request):
    productos = Producto.objects.all()  # Reutilizamos la lógica para obtener los productos
    context = {'productos': productos}
    return render(request, 'productos/carrito.html', context)