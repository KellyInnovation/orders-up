# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0006_auto_20161024_2014'),
        ('guest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='food_options',
            field=models.ForeignKey(to='kitchen.Kitchen', blank=True, null=True),
        ),
    ]
