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
