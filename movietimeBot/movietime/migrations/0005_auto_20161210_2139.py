# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietime', '0004_auto_20161210_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieproperties',
            name='actor_2_name',
            field=models.CharField(max_length=200),
        ),
    ]
