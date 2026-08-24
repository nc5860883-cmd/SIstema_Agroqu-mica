# Generated manually / Django migration

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        # 1. GrupoQuimico
        migrations.CreateModel(
            name='GrupoQuimico',
            fields=[
                ('ID_Grupo_quimico', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_grupo_quimico', models.CharField(max_length=60)),
                ('Descripcion_grupo_quimico', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Grupos Químicos',
            },
        ),
        # 2. TipoProducto
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('ID_Tipo_producto', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_producto', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Productos',
            },
        ),
        # 3. Proveedor
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('ID_Proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_proveedor', models.CharField(max_length=50, verbose_name='Nombre')),
                ('Telefono_proveedor', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('Direccion_proveedor', models.CharField(max_length=30, verbose_name='Dirección')),
                ('Email_proveedor', models.CharField(max_length=50, verbose_name='Email')),
                ('Estado_proveedor', models.CharField(max_length=20, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['Nombre_proveedor'],
            },
        ),
        # 4. TipoEmpleado
        migrations.CreateModel(
            name='TipoEmpleado',
            fields=[
                ('ID_Tipo_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_tipo_empleado', models.CharField(max_length=50)),
            ],
        ),
        # 5. TipoMovimiento
        migrations.CreateModel(
            name='TipoMovimiento',
            fields=[
                ('ID_Tipo_movimiento', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_tipo_movimiento', models.CharField(max_length=50)),
            ],
        ),
        # 6. Producto (depende de TipoProducto)
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('ID_Productos', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_producto', models.CharField(max_length=50)),
                ('Descripcion_producto', models.CharField(max_length=100)),
                ('Fecha_vencimiento', models.DateField()),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ID_Tipo_producto', models.ForeignKey(db_column='ID_Tipo_producto', on_delete=django.db.models.deletion.CASCADE, to='agroquimica.tipoproducto')),
            ],
        ),
        # 7. Empleado (depende de TipoEmpleado)
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('ID_Empleado', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_empleado', models.CharField(max_length=50)),
                ('Apellido_empleado', models.CharField(max_length=50)),
                ('Telefono_empleado', models.CharField(max_length=20)),
                ('Email_empleado', models.CharField(max_length=50)),
                ('ID_Tipo_empleado', models.ForeignKey(db_column='ID_Tipo_empleado', on_delete=django.db.models.deletion.CASCADE, to='agroquimica.tipoempleado')),
            ],
        ),
        # 8. Stock (depende de Producto)
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('ID_Stock', models.AutoField(primary_key=True, serialize=False)),
                ('Cantidad_stock', models.IntegerField()),
                ('Stock_minimo', models.IntegerField()),
                ('ID_Producto', models.ForeignKey(db_column='ID_Producto', on_delete=django.db.models.deletion.CASCADE, to='agroquimica.producto')),
            ],
        ),
        # 9. Alerta (depende de Stock)
        migrations.CreateModel(
            name='Alerta',
            fields=[
                ('ID_Alerta', models.AutoField(primary_key=True, serialize=False)),
                ('Mensaje', models.CharField(max_length=255)),
                ('Fecha_hora_alerta', models.DateTimeField()),
                ('ID_Stock', models.ForeignKey(db_column='ID_Stock', on_delete=django.db.models.deletion.CASCADE, to='agroquimica.stock')),
            ],
        ),
        # 10. MovimientoStock (depende de Empleado, TipoMovimiento, Stock)
        migrations.CreateModel(
            name='MovimientoStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_hora_movimiento', models.DateTimeField()),
                ('Cantidad', models.IntegerField()),
                ('ID_Empleado', models.ForeignKey(db_column='ID_Empleado', on_delete=django.db.models.deletion.CASCADE, to='agroquimica.empleado')),
                ('ID_Stock', models.ForeignKey(db_column='ID_Stock', on_delete=django.db.models.deletion.CASCADE, to='agroquimica.stock')),
                ('ID_Tipo_movimiento', models.ForeignKey(db_column='ID_Tipo_movimiento', on_delete=django.db.models.deletion.CASCADE, to='agroquimica.tipomovimiento')),
            ],
        ),
        # 11. ProductoXGrupoQuimico
        migrations.CreateModel(
            name='ProductoXGrupoQuimico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Grupo_quimico', models.ForeignKey(db_column='ID_Grupo_quimico', on_delete=django.db.models.deletion.CASCADE, to='agroquimica.grupoquimico')),
                ('ID_Producto', models.ForeignKey(db_column='ID_Producto', on_delete=django.db.models.deletion.CASCADE, to='agroquimica.producto')),
            ],
            options={
                'unique_together': {('ID_Producto', 'ID_Grupo_quimico')},
            },
        ),
        # 12. ProductoXProveedor
        migrations.CreateModel(
            name='ProductoXProveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Producto', models.ForeignKey(db_column='ID_Producto', on_delete=django.db.models.deletion.CASCADE, to='agroquimica.producto')),
                ('ID_Proveedores', models.ForeignKey(db_column='ID_Proveedores', on_delete=django.db.models.deletion.CASCADE, to='agroquimica.proveedor')),
            ],
            options={
                'unique_together': {('ID_Producto', 'ID_Proveedores')},
            },
        ),
    ]