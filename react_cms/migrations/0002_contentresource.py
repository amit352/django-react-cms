# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-09 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('react_cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Resource Name')),
                ('path', models.CharField(max_length=1000, verbose_name='Resource Path')),
                ('json', models.TextField(blank=True, null=True, verbose_name='Label')),
            ],
        ),
    ]
