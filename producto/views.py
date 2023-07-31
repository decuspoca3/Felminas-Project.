from django.shortcuts import render, redirect
from producto.models import Producto 
from producto.forms import ProductoForm, ProductoUpdateForm
from dbbackup.management.commands.dbbackup import Command as DbBackupCommand
import os

def hacer_backup(request):
    # Ruta donde deseas guardar el archivo de backup (asegúrate de que la carpeta "backups" exista)
    backup_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'base', 'backups')
    backup_file = f'{backup_dir}/nombre_del_archivo.bak'

    # Lógica para realizar el backup aquí
    verbosity_level = 1  # Establece un valor entero para verbosity, p. ej. 1
    DbBackupCommand().handle(filename=backup_file, verbosity=verbosity_level)

    return redirect('producto')
def producto_crear(request):
    titulo="Producto"
    if request.method== 'POST':
        form= ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form= ProductoForm()
       
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"producto/crear.html", context )


def producto_listar(request):
    titulo = "Producto"
    productos = Producto.objects.all()

    # Si se envía una solicitud POST, es una venta
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad_vendida = int(request.POST.get('cantidad', 0))

        try:
            # Obtener el detalle del producto seleccionado
            producto = Producto.objects.get(id=producto_id)

            # Verificar que el producto está en stock y la cantidad a vender no supere el stock disponible
            if producto.stock >= cantidad_vendida:
                # Actualizar el stock del producto después de la venta
                producto.stock -= cantidad_vendida
                producto.save()

                # Redirigir a la lista de productos después de realizar la venta
                return redirect('producto')

        except (Producto.DoesNotExist, ValueError):
            pass

    context = {
        "titulo": titulo,
        "productos": productos
    }

    return render(request, "producto/listar.html", context)





def producto_modificar(request,pk):
    titulo="Producto"
    producto= Producto.objects.get(id=pk)

    if request.method=='POST':
        form= ProductoUpdateForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form= ProductoUpdateForm(instance=producto)
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"producto/modificar.html", context)

def producto_eliminar(request,pk):
    producto= Producto.objects.filter(id=pk)
    producto.update(
        estado="0"
    )
    return redirect('producto')
