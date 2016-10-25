# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0003_hostess_checkin_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostess',
            name='seating_requests',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
