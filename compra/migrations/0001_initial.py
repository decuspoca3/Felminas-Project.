# Generated by Django 4.2.1 on 2023-10-09 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(verbose_name='Número de Ficha')),
                ('fecha_ingreso', models.DateField(help_text='DD/MM/AAAA', verbose_name='Fecha de Ingreso')),
                ('fecha_productiva', models.DateField(help_text='DD/MM/AAAA', verbose_name='Fecha de Etapa Productiva')),
                ('fecha_final', models.DateField(help_text='DD/MM/AAAA', verbose_name='Fecha de Salida')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'Fichas',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=uuid.uuid4, editable=False, max_length=100, unique=True)),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de Creación')),
                ('Empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Empleado')),
                ('aprendiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Proveedor', to=settings.AUTH_USER_MODEL, verbose_name='Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Integrantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='cantidad')),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Unitario')),
                ('valortotal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='valor total')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compra.proyecto', verbose_name='Grupo')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto', verbose_name='Producto')),
            ],
        ),
    ]
