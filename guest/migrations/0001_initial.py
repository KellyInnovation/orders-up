# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=70, blank=True, null=True)),
                ('last_name', models.CharField(max_length=70, blank=True, null=True)),
                ('drink', models.CharField(max_length=30, default='water')),
                ('appetizer', models.CharField(max_length=100, blank=True, null=True)),
                ('entree', models.CharField(max_length=50, blank=True, null=True)),
                ('side_item', models.CharField(max_length=100, blank=True, null=True)),
                ('dessert', models.CharField(max_length=100, blank=True, null=True)),
                ('special_instructions', models.CharField(max_length=500, blank=True, null=True)),
                ('party_id', models.ForeignKey(default='1', to='hostess.Hostess')),
            ],
        ),
    ]
