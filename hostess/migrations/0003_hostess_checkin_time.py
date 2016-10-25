# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0002_auto_20161024_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostess',
            name='checkin_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 10, 25, 18, 11, 29, 73346, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
