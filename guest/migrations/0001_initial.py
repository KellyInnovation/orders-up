# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=70, null=True)),
                ('last_name', models.CharField(blank=True, max_length=70, null=True)),
                ('party_number', models.IntegerField()),
                ('party_url', models.CharField(max_length=300)),
                ('drink', models.CharField(max_length=30, default='water')),
                ('entree', models.CharField(blank=True, max_length=50, null=True)),
                ('side_item', models.CharField(blank=True, max_length=100, null=True)),
                ('dessert', models.CharField(blank=True, max_length=100, null=True)),
                ('special_instructions', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
