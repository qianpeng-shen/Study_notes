# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-27 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_author_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': '夫人',
                'db_table': 'wife',
                'verbose_name': '夫人',
            },
        ),
    ]
