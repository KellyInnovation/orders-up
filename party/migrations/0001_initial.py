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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('drink', models.CharField(max_length=30, default='water')),
                ('food', models.CharField(blank=True, null=True, max_length=400)),
                ('order_price', models.DecimalField(max_digits=1000, decimal_places=0, default=0)),
                ('special_instructions', models.CharField(blank=True, null=True, max_length=500)),
                ('hostess', models.OneToOneField(to='hostess.Hostess')),
            ],
        ),
    ]
