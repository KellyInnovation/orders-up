# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0005_auto_20161026_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostess',
            name='unique_party_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='hostess',
            name='unique_party_url',
            field=models.URLField(blank=True),
        ),
    ]
