# Generated by Django 5.0.6 on 2024-06-10 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Producto',
            new_name='productos',
        ),
    ]
