# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen_order', '0001_initial'),
        ('party', '0001_initial'),
        ('kitchen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen',
            name='orders',
            field=models.ManyToManyField(through='kitchen_order.KitchenOrder', to='party.Party'),
        ),
    ]
