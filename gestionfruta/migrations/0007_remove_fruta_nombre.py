# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-29 10:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionfruta', '0006_auto_20160629_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fruta',
            name='nombre',
        ),
    ]
