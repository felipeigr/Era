from django.contrib import admin
from .models import Producto,Carrito,CarritoProducto, Venta
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'juego_producto')
    list_filter = ('juego_producto',)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Carrito)
admin.site.register(CarritoProducto)
admin.site.register(Venta)