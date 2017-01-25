# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('count', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=200)),
                ('delivery_date', models.DateTimeField(verbose_name='date published')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
