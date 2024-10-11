# Generated by Django 5.0.6 on 2024-06-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_web', '0005_boleta_nombre_receptor_boleta_rut_receptor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='estado',
            field=models.CharField(choices=[('CANCELADO', 'Cancelado'), ('COMPLETADO', 'Completado'), ('ENVIO', 'Envio'), ('ALMACEN', 'Almacen')], default='ALMACEN', max_length=20, verbose_name='estado'),
        ),
        migrations.AlterField(
            model_name='boleta',
            name='nombre_receptor',
            field=models.CharField(max_length=100, verbose_name='Nombre del Receptor'),
        ),
        migrations.AlterField(
            model_name='boleta',
            name='rut_receptor',
            field=models.CharField(max_length=12, verbose_name='RUT del Receptor'),
        ),
    ]
