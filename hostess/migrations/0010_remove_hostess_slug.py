# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0009_hostess_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostess',
            name='slug',
        ),
    ]
