# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0003_auto_20161026_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='food_options',
            field=models.ForeignKey(to='kitchen.Kitchen', null=True, blank=True),
        ),
    ]
