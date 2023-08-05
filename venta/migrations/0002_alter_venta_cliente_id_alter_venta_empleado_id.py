# Generated by Django 4.1.7 on 2023-08-03 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_alter_salario_fecha_alter_usuario_rol'),
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='cliente_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas_realizadas', to='usuario.usuario', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='empleado_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas_atendidas', to='usuario.usuario', verbose_name='Empleado'),
        ),
    ]
