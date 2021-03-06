# Generated by Django 3.2.5 on 2022-04-03 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_delete_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False, verbose_name='id producto')),
                ('nombre_producto', models.CharField(max_length=128, verbose_name='nombre producto')),
                ('tipo_producto', models.CharField(max_length=128, verbose_name='tipo producto')),
                ('marca_producto', models.CharField(max_length=128, verbose_name='marca producto')),
                ('desc_producto', models.CharField(default='none', max_length=700, verbose_name='descripcion producto')),
                ('precio_producto', models.IntegerField(verbose_name='precio producto')),
                ('imagen_producto', models.ImageField(default='static/core/img/default.png', upload_to='core', verbose_name='imagen producto')),
                ('carousel', models.ImageField(default='/core/default.jpg', upload_to='core', verbose_name='carousel1')),
                ('carousel2', models.ImageField(default='/core/default.jpg', upload_to='core', verbose_name='carousel2')),
                ('carousel3', models.ImageField(default='core/default.jpg', upload_to='core', verbose_name='carousel3')),
                ('carousel4', models.ImageField(default='core/default.jpg', upload_to='core', verbose_name='carousel4')),
            ],
        ),
    ]
