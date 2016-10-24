# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostess',
            name='seating_requests',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
