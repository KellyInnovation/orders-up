# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0003_auto_20161103_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='order_price',
            field=models.DecimalField(default=0, decimal_places=0, max_digits=1000),
        ),
    ]
