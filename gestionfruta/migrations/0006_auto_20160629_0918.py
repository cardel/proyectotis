# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-29 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionfruta', '0005_auto_20160629_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AddField(
            model_name='fruta',
            name='imagen',
            field=models.ImageField(null=True, upload_to='frutas'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='direccion',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='telefono',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='finca',
            name='departamento',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='finca',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='finca',
            name='imagen',
            field=models.ImageField(default='', null=True, upload_to='finca'),
        ),
    ]
