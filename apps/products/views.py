from django.shortcuts import render, get_object_or_404,redirect
from .models import Producto,Categoria

# LISTAR PRODUCTO
def listado_productos(request):
    productos = Producto.objects.all()
    print(f"Cantidad {productos}")
    return render(request, 'productos/listado_productos.html', {'productos': productos})

# CREAR PRODUCTO
def crear_producto(request):
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        categoria_id = request.POST.get('categoria')

        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            categoria_id=categoria_id
        )

        return redirect('listado_productos')

    return render(request, 'productos/crear_producto.html', {
        'categorias': categorias
    })


# EDITAR PRODUCTO
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.categoria_id = request.POST.get('categoria')
        producto.save()

        return redirect('listado_productos')

    return render(request, 'products/editar.html', {
        'producto': producto,
        'categorias': categorias
    })


# ELIMINAR PRODUCTO
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.delete()
        return redirect('listado_productos')

    return render(request, 'products/eliminar.html', {
        'producto': producto
    })




def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'productos/detalle_productos.html', {'producto': producto})






# ===== CRUD CATEGORÍAS =====

def lista_categorias(request):
    categorias = Categoria.objects.all()
    print(f"Categorias {categorias}")
    return render(request, 'categorias/lista_categorias.html', {
        'categorias': categorias
    })


def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        Categoria.objects.create(nombre=nombre)
        return redirect('lista_categorias')

    return render(request, 'categorias/crear_categoria.html')


def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        categoria.nombre = request.POST.get('nombre')
        categoria.save()
        return redirect('lista_categorias')

    return render(request, 'categorias/editar_categoria.html', {
        'categoria': categoria
    })


def eliminar_categoria(request, categoria_id):
    print(f"Eliminando el id {categoria_id}")

    categoria = get_object_or_404(Categoria, id=categoria_id)
    print(categoria)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')

    return render(request, 'categorias/eliminar_categoria.html', {
        'categoria': categoria
    })