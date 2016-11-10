# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('drink', models.CharField(max_length=30, default='water')),
                ('food', models.CharField(max_length=400, null=True, blank=True)),
                ('order_price', models.DecimalField(max_digits=1000, default=0, decimal_places=0)),
                ('special_instructions', models.CharField(max_length=500, null=True, blank=True)),
                ('hostess', models.OneToOneField(blank=True, to='hostess.Hostess', null=True)),
            ],
        ),
    ]
