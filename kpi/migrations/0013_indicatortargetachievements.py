# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2019-08-08 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0012_auto_20190807_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicatorTargetAchievements',
            fields=[
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('achievedtarget', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='kpi.IndicatorTargets')),
            ],
            options={
                'db_table': 'indicatortargetachievements',
            },
        ),
    ]
