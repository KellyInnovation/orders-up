# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0008_auto_20161026_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchen',
            name='item_price',
            field=models.DecimalField(max_digits=10000, decimal_places=0),
        ),
    ]
