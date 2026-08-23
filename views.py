from django.shortcuts import render
from .models import (
    GrupoQuimico,
    TipoProducto,
    Producto,
    Proveedor,
    ProductoXGrupoQuimico,
    ProductoXProveedor,
    Stock,
    Alerta,
    TipoEmpleado,
    Empleado,
    TipoMovimiento,
    MovimientoStock,
)


def lista_grupos_quimicos(request):
    grupos_quimicos = GrupoQuimico.objects.all()
    total = grupos_quimicos.count()
    return render(request, 'agroquimica/lista_grupos_quimicos.html', {
        'grupos_quimicos': grupos_quimicos,
        'total': total
    })


def lista_tipos_productos(request):
    tipos_productos = TipoProducto.objects.all()
    total = tipos_productos.count()
    return render(request, 'agroquimica/lista_tipos_productos.html', {
        'tipos_productos': tipos_productos,
        'total': total
    })


def lista_productos(request):
    productos = Producto.objects.select_related('ID_Tipo_producto').all()
    total = productos.count()
    return render(request, 'agroquimica/lista_productos.html', {
        'productos': productos,
        'total': total
    })


def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    total = proveedores.count()
    return render(request, 'agroquimica/lista_proveedores.html', {
        'proveedores': proveedores,
        'total': total
    })


def lista_productos_x_grupos(request):
    productos_x_grupos = ProductoXGrupoQuimico.objects.select_related('ID_Producto', 'ID_Grupo_quimico').all()
    total = productos_x_grupos.count()
    return render(request, 'agroquimica/lista_productos_x_grupos.html', {
        'productos_x_grupos': productos_x_grupos,
        'total': total
    })


def lista_productos_x_proveedores(request):
    productos_x_proveedores = ProductoXProveedor.objects.select_related('ID_Producto', 'ID_Proveedores').all()
    total = productos_x_proveedores.count()
    return render(request, 'agroquimica/lista_productos_x_proveedores.html', {
        'productos_x_proveedores': productos_x_proveedores,
        'total': total
    })


def lista_stock(request):
    stocks = Stock.objects.select_related('ID_Producto').all()
    total = stocks.count()
    return render(request, 'agroquimica/lista_stock.html', {
        'stocks': stocks,
        'total': total
    })


def lista_alertas(request):
    alertas = Alerta.objects.select_related('ID_Stock__ID_Producto').all()
    total = alertas.count()
    return render(request, 'agroquimica/lista_alertas.html', {
        'alertas': alertas,
        'total': total
    })


def lista_tipos_empleados(request):
    tipos_empleados = TipoEmpleado.objects.all()
    total = tipos_empleados.count()
    return render(request, 'agroquimica/lista_tipos_empleados.html', {
        'tipos_empleados': tipos_empleados,
        'total': total
    })


def lista_empleados(request):
    empleados = Empleado.objects.select_related('ID_Tipo_empleado').all()
    total = empleados.count()
    return render(request, 'agroquimica/lista_empleados.html', {
        'empleados': empleados,
        'total': total
    })


def lista_tipos_movimientos(request):
    tipos_movimientos = TipoMovimiento.objects.all()
    total = tipos_movimientos.count()
    return render(request, 'agroquimica/lista_tipos_movimientos.html', {
        'tipos_movimientos': tipos_movimientos,
        'total': total
    })


def lista_movimientos_stock(request):
    movimientos = MovimientoStock.objects.select_related('ID_Empleado', 'ID_Tipo_movimiento', 'ID_Stock').all()
    total = movimientos.count()
    return render(request, 'agroquimica/lista_movimientos_stock.html', {
        'movimientos': movimientos,
        'total': total
    })