from django.db import models

class GrupoQuimico(models.Model):
    ID_Grupo_quimico = models.AutoField(primary_key=True)
    Nombre_grupo_quimico = models.CharField(max_length=60)
    Descripcion_grupo_quimico = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Grupos Químicos"

    def __str__(self):
        return self.Nombre_grupo_quimico


class TipoProducto(models.Model):
    ID_Tipo_producto = models.AutoField(primary_key=True)
    Nombre_producto = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Tipos de Productos"

    def __str__(self):
        return self.Nombre_producto


class Producto(models.Model):
    ID_Productos = models.AutoField(primary_key=True)
    ID_Tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE, db_column='ID_Tipo_producto')
    Nombre_producto = models.CharField(max_length=50)
    Descripcion_producto = models.CharField(max_length=100)
    Fecha_vencimiento = models.DateField()
    Precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Nombre_producto


class Proveedor(models.Model):
    ID_Proveedor = models.AutoField(primary_key=True)
    Nombre_proveedor = models.CharField('Nombre', max_length=50)
    Telefono_proveedor = models.CharField('Teléfono', max_length=20)
    Direccion_proveedor = models.CharField('Dirección', max_length=30)
    Email_proveedor = models.CharField('Email', max_length=50)
    Estado_proveedor = models.CharField('Estado', max_length=20)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['Nombre_proveedor']

    def __str__(self):
        return f"{self.Nombre_proveedor} ({self.Estado_proveedor})"


class ProductoXGrupoQuimico(models.Model):
    ID_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='ID_Producto')
    ID_Grupo_quimico = models.ForeignKey(GrupoQuimico, on_delete=models.CASCADE, db_column='ID_Grupo_quimico')

    class Meta:
        unique_together = (('ID_Producto', 'ID_Grupo_quimico'),)


class ProductoXProveedor(models.Model):
    ID_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='ID_Producto')
    ID_Proveedores = models.ForeignKey(Proveedor, on_delete=models.CASCADE, db_column='ID_Proveedores')

    class Meta:
        unique_together = (('ID_Producto', 'ID_Proveedores'),)


class Stock(models.Model):
    ID_Stock = models.AutoField(primary_key=True)
    ID_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='ID_Producto')
    Cantidad_stock = models.IntegerField()
    Stock_minimo = models.IntegerField()


class Alerta(models.Model):
    ID_Alerta = models.AutoField(primary_key=True)
    ID_Stock = models.ForeignKey(Stock, on_delete=models.CASCADE, db_column='ID_Stock')
    Mensaje = models.CharField(max_length=255)
    Fecha_hora_alerta = models.DateTimeField()


class TipoEmpleado(models.Model):
    ID_Tipo_empleado = models.AutoField(primary_key=True)
    Nombre_tipo_empleado = models.CharField(max_length=50)


class Empleado(models.Model):
    ID_Empleado = models.AutoField(primary_key=True)
    Nombre_empleado = models.CharField(max_length=50)
    Apellido_empleado = models.CharField(max_length=50)
    Telefono_empleado = models.CharField(max_length=20)
    Email_empleado = models.CharField(max_length=50)
    ID_Tipo_empleado = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE, db_column='ID_Tipo_empleado')


class TipoMovimiento(models.Model):
    ID_Tipo_movimiento = models.AutoField(primary_key=True)
    Nombre_tipo_movimiento = models.CharField(max_length=50)


class MovimientoStock(models.Model):
    ID_Movimiento_stock = models.AutoField(primary_key=True)
    ID_Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, db_column='ID_Empleado')
    ID_Tipo_movimiento = models.ForeignKey(TipoMovimiento, on_delete=models.CASCADE, db_column='ID_Tipo_movimiento')
    ID_Stock = models.ForeignKey(Stock, on_delete=models.CASCADE, db_column='ID_Stock')
    Fecha_hora_movimiento = models.DateTimeField()
    Cantidad = models.IntegerField()