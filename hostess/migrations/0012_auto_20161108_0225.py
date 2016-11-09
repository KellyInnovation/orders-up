# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0011_auto_20161107_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostess',
            name='checkin_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
