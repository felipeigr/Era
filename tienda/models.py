from django.db import models as m
from django.contrib.auth.models import User

class Producto(m.Model):
    JUEGOS = [
        ('LOL', 'League of Legends'),
        ('VAL', 'Valorant'),
        ('TFT', 'Teamfight Tactics'),
        ('WR', 'Wild Rift'),
        ('PTS', 'Puntos Riot (Valorant/LoL)')
    ]
    id = m.AutoField(primary_key=True)
    nombre = m.CharField(max_length=16, null=False)
    descripcion = m.CharField(max_length=250, null=False)
    foto_producto = m.ImageField(blank=True, null=False)
    precio = m.BigIntegerField(null=False, default=0)
    juego_producto = m.CharField(max_length=3, choices=JUEGOS, default='')

    class Meta:
        managed = True
        db_table = "Productos"

class Carrito(m.Model):
    propietario_carrito = m.OneToOneField(User, on_delete=m.CASCADE, null=True, blank=True)  # Cambia Usuario a User
    productos = m.ManyToManyField(Producto, through='CarritoProducto')

    class Meta:
        managed = True
        db_table = "Carrito"

class CarritoProducto(m.Model):
    carrito = m.ForeignKey(Carrito, on_delete=m.CASCADE)
    producto = m.ForeignKey(Producto, on_delete=m.CASCADE)
    cantidad = m.PositiveIntegerField(default=1)
    total = m.IntegerField(default=0, null=False)

    class Meta:
        unique_together = ('carrito', 'producto')
        managed = True
        db_table = "CarritoProducto"



class Venta(m.Model):
    id_venta = m.AutoField(primary_key=True)
    usuario = m.ForeignKey(User, on_delete=m.CASCADE)
    producto = m.ForeignKey(Producto, on_delete=m.CASCADE)
    cantidad = m.PositiveIntegerField(default=1)
    monto_total = m.IntegerField(default=0, null=False)
    fecha_venta = m.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = "Venta"