# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-06 11:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('aircraft_type', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name=b'airport name')),
            ],
        ),
        migrations.CreateModel(
            name='AirFlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField(db_index=True, verbose_name=b'departure time')),
                ('arrival_time', models.DateTimeField(db_index=True, verbose_name=b'arrival time')),
                ('travel_time', models.PositiveIntegerField(db_index=True, verbose_name=b'travel time')),
                ('aircraft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.Aircraft')),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('airport_name', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name=b'airport name')),
            ],
        ),
        migrations.AddField(
            model_name='airflight',
            name='airport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.Airport'),
        ),
    ]
