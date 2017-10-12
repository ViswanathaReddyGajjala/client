# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 06:13
from __future__ import unicode_literals

import datetime
import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='Rice', max_length=50)),
                ('Year', models.IntegerField()),
                ('Seasons', models.CharField(choices=[('S', 'Summer'), ('W', 'Winter'), ('M', 'Monsoon')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Farms',
            fields=[
                ('FID', models.AutoField(primary_key=True, serialize=False)),
                ('plot', django.contrib.gis.db.models.fields.PolygonField(geography=True, srid=4326)),
                ('area', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('HID', models.AutoField(primary_key=True, serialize=False)),
                ('income', models.FloatField(default=0.0)),
                ('point', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(1, 1), null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('PID', models.AutoField(primary_key=True, serialize=False)),
                ('Age', models.IntegerField(default=0)),
                ('Name', models.CharField(default='', max_length=30)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('HID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.Houses')),
            ],
        ),
        migrations.CreateModel(
            name='Wells',
            fields=[
                ('WID', models.AutoField(primary_key=True, serialize=False)),
                ('point', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(1, 1), srid=4326)),
                ('AvgYield', models.DecimalField(decimal_places=4, max_digits=7)),
                ('HID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.Houses')),
            ],
        ),
        migrations.CreateModel(
            name='Yields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Yield', models.FloatField(default=0.0)),
                ('measured_date', models.DateField(default=datetime.date.today)),
                ('WID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.Wells')),
            ],
        ),
        migrations.AddField(
            model_name='farms',
            name='HID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.Houses'),
        ),
        migrations.AddField(
            model_name='crops',
            name='FID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.Farms'),
        ),
    ]
