# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-23 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('react_cms', '0005_contentresource_rendered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentresource',
            name='path',
            field=models.CharField(max_length=191, unique=True, verbose_name='Resource Path'),
        ),
    ]
