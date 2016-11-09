# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0010_remove_hostess_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostess',
            name='checkin_time',
            field=models.DurationField(default=datetime.timedelta(0, 1800)),
        ),
    ]
