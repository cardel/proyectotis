# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-29 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionfruta', '0008_auto_20160629_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruta',
            name='nombre',
            field=models.CharField(default='', max_length=120),
        ),
    ]
