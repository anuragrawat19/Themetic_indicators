# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2019-08-06 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0007_auto_20190806_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicatortargets',
            name='indicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indicatortarget', to='kpi.Indicators'),
        ),
    ]