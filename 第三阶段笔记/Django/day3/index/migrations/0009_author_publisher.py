# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-26 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20180626_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='publisher',
            field=models.ManyToManyField(to='index.Publisher'),
        ),
    ]
