# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0008_remove_hostess_unique_party_url'),
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='id',
        ),
        migrations.AddField(
            model_name='party',
            name='hostess',
            field=models.OneToOneField(serialize=False, to='hostess.Hostess', default=1, primary_key=True),
            preserve_default=False,
        ),
    ]
