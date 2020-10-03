# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True,
                    primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('display_name', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=256)),
                ('website',  models.URLField()),
                ('logo_url',  models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True,
                    primary_key=True)),
                ('station', models.ForeignKey(
                    'Station', on_delete=models.CASCADE)),
                ('city', models.CharField(max_length=128)),
                ('street', models.CharField(max_length=256)),
                ('number', models.PositiveSmallIntegerField()),
                ('zip', models.DecimalField(max_digits=5, decimal_places=0)),
                ('email', models.EmailField()),
                ('phone', models.CharField(max_length=32)),
                ('location_latitude', models.DecimalField(
                    max_digits=10, decimal_places=7)),
                ('location_longitude', models.DecimalField(
                    max_digits=10, decimal_places=7)),
                ('open_from', models.TimeField()),
                ('open_to', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CableTransmitter',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True,
                    primary_key=True)),
                ('station', models.ForeignKey(
                    'Station', on_delete=models.CASCADE)),
                ('frequency', models.DecimalField(
                    max_digits=6, decimal_places=2)),
                ('operator', models.CharField(max_length=128)),
                ('transmission_from', models.TimeField()),
                ('transmission_to', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UKWTransmitter',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True,
                    primary_key=True)),
                ('station', models.ForeignKey(
                    to='frapp.Station', on_delete=models.CASCADE)),
                ('frequency', models.DecimalField(
                    max_digits=6, decimal_places=2)),
                ('city', models.CharField(max_length=128)),
                ('operator', models.CharField(max_length=128)),
                ('rds_id', models.CharField(max_length=64)),
                ('location_latitude', models.DecimalField(
                    max_digits=10, decimal_places=7)),
                ('location_longitude', models.DecimalField(
                    max_digits=10, decimal_places=7)),
                ('transmission_power', models.PositiveSmallIntegerField()),
                ('transmission_range', models.PositiveSmallIntegerField()),
                ('transmission_from', models.TimeField()),
                ('transmission_to', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='StreamTransmitter',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False,
                                        auto_created=True,
                                        primary_key=True)),
                ('station', models.ForeignKey('Station',
                                              on_delete=models.CASCADE)),
                ('url',  models.URLField()),
                ('content_type', models.PositiveSmallIntegerField()),
                ('bitrate', models.DecimalField(max_digits=3,
                                                decimal_places=0)),
                ('transmission_from', models.TimeField()),
                ('transmission_to', models.TimeField()),
            ],
        ),
    ]
