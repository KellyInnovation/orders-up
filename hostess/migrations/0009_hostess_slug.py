# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0008_remove_hostess_unique_party_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostess',
            name='slug',
            field=models.SlugField(default='wright-1'),
            preserve_default=False,
        ),
    ]
