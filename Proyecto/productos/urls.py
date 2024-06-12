from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('valo/', views.valo, name='valo'),
    path('lol/', views.lol, name='lol'),
]

