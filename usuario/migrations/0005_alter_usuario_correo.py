# Generated by Django 4.2.2 on 2023-11-01 22:42

from django.db import migrations, models
import usuario.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_alter_salario_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.CharField(max_length=40, validators=[usuario.models.unique_correo], verbose_name='Correo Electrónico'),
        ),
    ]
