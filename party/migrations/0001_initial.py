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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('drink', models.CharField(max_length=30, default='water')),
                ('food', models.CharField(max_length=400, blank=True, null=True)),
                ('order_price', models.DecimalField(decimal_places=0, max_digits=1000, default=0)),
                ('special_instructions', models.CharField(max_length=500, blank=True, null=True)),
                ('hostess', models.OneToOneField(to='hostess.Hostess')),
            ],
        ),
    ]
