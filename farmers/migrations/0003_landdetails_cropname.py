# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2019-08-13 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0002_auto_20190812_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='landdetails',
            name='cropname',
            field=models.CharField(default='Wheat', max_length=100),
        ),
    ]
