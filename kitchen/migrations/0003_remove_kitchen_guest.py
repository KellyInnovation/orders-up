# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0002_kitchen_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitchen',
            name='guest',
        ),
    ]
