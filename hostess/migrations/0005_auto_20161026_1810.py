# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0004_auto_20161025_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostess',
            name='unique_party_id',
        ),
        migrations.RemoveField(
            model_name='hostess',
            name='unique_party_url',
        ),
    ]
