from django.contrib import admin
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


@admin.register(GrupoQuimico)
class GrupoQuimicoAdmin(admin.ModelAdmin):
    list_display = ('ID_Grupo_quimico', 'Nombre_grupo_quimico', 'Descripcion_grupo_quimico')
    search_fields = ('Nombre_grupo_quimico',)


@admin.register(TipoProducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('ID_Tipo_producto', 'Nombre_producto')
    search_fields = ('Nombre_producto',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('ID_Productos', 'Nombre_producto', 'ID_Tipo_producto', 'Fecha_vencimiento', 'Precio')
    search_fields = ('Nombre_producto', 'Descripcion_producto')
    list_filter = ('ID_Tipo_producto', 'Fecha_vencimiento')


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('ID_Proveedor', 'Nombre_proveedor', 'Telefono_proveedor', 'Email_proveedor', 'Estado_proveedor')
    search_fields = ('Nombre_proveedor', 'Email_proveedor')
    list_filter = ('Estado_proveedor',)


@admin.register(ProductoXGrupoQuimico)
class ProductoXGrupoQuimicoAdmin(admin.ModelAdmin):
    list_display = ('ID_Producto', 'ID_Grupo_quimico')
    list_filter = ('ID_Grupo_quimico',)


@admin.register(ProductoXProveedor)
class ProductoXProveedorAdmin(admin.ModelAdmin):
    list_display = ('ID_Producto', 'ID_Proveedores')
    list_filter = ('ID_Proveedores',)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('ID_Stock', 'ID_Producto', 'Cantidad_stock', 'Stock_minimo')
    search_fields = ('ID_Producto__Nombre_producto',)


@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ('ID_Alerta', 'ID_Stock', 'Mensaje', 'Fecha_hora_alerta')
    search_fields = ('Mensaje',)
    list_filter = ('Fecha_hora_alerta',)


@admin.register(TipoEmpleado)
class TipoEmpleadoAdmin(admin.ModelAdmin):
    list_display = ('ID_Tipo_empleado', 'Nombre_tipo_empleado')
    search_fields = ('Nombre_tipo_empleado',)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('ID_Empleado', 'Nombre_empleado', 'Apellido_empleado', 'Telefono_empleado', 'Email_empleado', 'ID_Tipo_empleado')
    search_fields = ('Nombre_empleado', 'Apellido_empleado', 'Email_empleado')
    list_filter = ('ID_Tipo_empleado',)


@admin.register(TipoMovimiento)
class TipoMovimientoAdmin(admin.ModelAdmin):
    list_display = ('ID_Tipo_movimiento', 'Nombre_tipo_movimiento')
    search_fields = ('Nombre_tipo_movimiento',)


@admin.register(MovimientoStock)
class MovimientoStockAdmin(admin.ModelAdmin):
    list_display = ('ID_Movimiento_stock', 'ID_Empleado', 'ID_Tipo_movimiento', 'ID_Stock', 'Cantidad', 'Fecha_hora_movimiento')
    search_fields = ('ID_Empleado__Nombre_empleado', 'ID_Empleado__Apellido_empleado')
    list_filter = ('ID_Tipo_movimiento', 'Fecha_hora_movimiento')