# Generated by Django 5.0.6 on 2024-06-10 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_rename_producto_productos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='productos',
            new_name='Producto',
        ),
    ]