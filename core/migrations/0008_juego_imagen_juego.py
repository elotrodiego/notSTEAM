# Generated by Django 3.2.3 on 2021-06-16 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_juego_imagen_juego'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='imagen_juego',
            field=models.ImageField(default='static/core/img/default.png', upload_to='core', verbose_name='imagen del juego'),
        ),
    ]