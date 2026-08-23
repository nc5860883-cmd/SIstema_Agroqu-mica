from django.db import models

class GrupoQuimico(models.Model):
    id_grupo_quimico = models.AutoField(primary_key=True)
    nombre_grupo_quimico = models.CharField(max_length=60)
    descripcion_grupo_quimico = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Grupos Químicos"

    def __str__(self):
        return self.nombre_grupo_quimico


class TipoProducto(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Tipos de Productos"

    def __str__(self):
        return self.nombre_producto


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=50)
    descripcion_producto = models.CharField(max_length=100)
    fecha_vencimiento = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_producto


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField('Nombre', max_length=50)
    telefono_proveedor = models.CharField('Teléfono', max_length=20)
    direccion_proveedor = models.CharField('Dirección', max_length=30)
    email_proveedor = models.CharField('Email', max_length=50)
    estado_proveedor = models.CharField('Estado', max_length=20)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre_proveedor']

    def __str__(self):
        return f"{self.nombre_proveedor} ({self.estado_proveedor})"


class ProductoXGrupoQuimico(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    grupo_quimico = models.ForeignKey(GrupoQuimico, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('producto', 'grupo_quimico'),)


class ProductoXProveedor(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('producto', 'proveedor'),)


class Stock(models.Model):
    id_stock = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_stock = models.IntegerField()
    stock_minimo = models.IntegerField()


class Alerta(models.Model):
    id_alerta = models.AutoField(primary_key=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=255)
    fecha_hora_alerta = models.DateTimeField(auto_now_add=True)


class TipoEmpleado(models.Model):
    id_tipo_empleado = models.AutoField(primary_key=True)
    nombre_tipo_empleado = models.CharField(max_length=50)


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=50)
    apellido_empleado = models.CharField(max_length=50)
    telefono_empleado = models.CharField(max_length=20)
    email_empleado = models.CharField(max_length=50)
    tipo_empleado = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)


class TipoMovimiento(models.Model):
    id_tipo_movimiento = models.AutoField(primary_key=True)
    nombre_tipo_movimiento = models.CharField(max_length=50)


class MovimientoStock(models.Model):
    id_movimiento_stock = models.AutoField(primary_key=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo_movimiento = models.ForeignKey(TipoMovimiento, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    fecha_hora_movimiento = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()