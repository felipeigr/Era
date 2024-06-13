from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('valo/', views.valo, name='valo'),
    path('lol/', views.lol, name='lol'),
    path('login/', views.login, name='login'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('rp/', views.rp, name='rp'),
    path('carrito/', views.carrito, name='carrito'),
    path('registro/', views.registro, name='registro'),
]

