# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0002_guest_food_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='food_options',
            field=models.ForeignKey(null=True, blank=True, related_name='menus', to='kitchen.Kitchen'),
        ),
    ]
