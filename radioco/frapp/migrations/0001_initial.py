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
                ('open_from', models.TimeField()),
                ('open_to', models.TimeField()),
            ],
        ),
    ]
