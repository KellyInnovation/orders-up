# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0007_remove_hostess_unique_party_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostess',
            name='unique_party_url',
        ),
    ]
