# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0009_auto_20161027_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchen',
            name='item_price',
            field=models.DecimalField(decimal_places=0, max_digits=1000),
        ),
    ]
