# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0006_auto_20161026_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostess',
            name='unique_party_id',
        ),
    ]
