# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2019-08-07 07:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0009_auto_20190806_0933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indicators',
            options={'ordering': ['id'], 'verbose_name_plural': 'Indicators'},
        ),
        migrations.AlterModelOptions(
            name='themetics',
            options={'ordering': ['id'], 'verbose_name_plural': 'Themetics'},
        ),
    ]