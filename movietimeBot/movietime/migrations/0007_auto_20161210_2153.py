# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 21:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movietime', '0006_auto_20161210_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieproperties',
            old_name='genres',
            new_name='genres_ignore',
        ),
        migrations.RenameField(
            model_name='movieproperties',
            old_name='plot_keywords',
            new_name='plot_keywords_ignore',
        ),
    ]
