# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2019-08-09 05:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialYears',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('year', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ['year'],
                'db_table': 'financialyear',
                'verbose_name_plural': 'Financial Years',
            },
        ),
        migrations.CreateModel(
            name='Indicators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('indicatorname', models.CharField(max_length=100)),
                ('shortcode', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'indicators',
                'verbose_name_plural': 'Indicators',
            },
        ),
        migrations.CreateModel(
            name='IndicatorTargets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('quarter', models.IntegerField(choices=[(1, 'Quarter 1'), (2, 'Quarter 2'), (3, 'Quarter 3'), (4, 'Quarter 4')], default=1)),
                ('target', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'indicatortargets',
                'verbose_name_plural': 'IndicatorTargets',
            },
        ),
        migrations.CreateModel(
            name='Themetics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('themeticname', models.CharField(max_length=50, unique=True)),
                ('code', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'themetics',
                'verbose_name_plural': 'Themetics',
            },
        ),
        migrations.CreateModel(
            name='IndicatorTargetAchievements',
            fields=[
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('indicatortarget', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='target_achieved', serialize=False, to='kpi.IndicatorTargets')),
                ('achievedtarget', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'indicatortargetachievements',
            },
        ),
        migrations.AddField(
            model_name='indicatortargets',
            name='financialyear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finance_year', to='kpi.FinancialYears'),
        ),
        migrations.AddField(
            model_name='indicatortargets',
            name='indicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indicator_target', to='kpi.Indicators'),
        ),
        migrations.AddField(
            model_name='indicators',
            name='themetic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theme', to='kpi.Themetics'),
        ),
    ]
