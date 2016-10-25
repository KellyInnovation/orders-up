# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0001_initial'),
        ('kitchen', '0004_auto_20161024_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen',
            name='guest_order',
            field=models.ManyToManyField(to='guest.Guest', blank=True, null=True),
        ),
    ]
