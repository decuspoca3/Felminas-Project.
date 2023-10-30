# Generated by Django 4.2.1 on 2023-10-14 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_alter_salario_usuario'),
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='empleado_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='rol',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Empleado', 'Empleado')], max_length=10, verbose_name='Rol'),
        ),
    ]
