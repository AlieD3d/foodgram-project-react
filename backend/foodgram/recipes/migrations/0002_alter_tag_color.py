# Generated by Django 3.2.13 on 2022-12-03 18:21

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=colorfield.fields.ColorField(default='#ff0000', image_field=None, max_length=18, samples=None, verbose_name='Цветовой HEX-код'),
        ),
    ]
