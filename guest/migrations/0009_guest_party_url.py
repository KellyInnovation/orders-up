# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0006_auto_20161026_1811'),
        ('guest', '0008_remove_guest_party_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='party_url',
            field=models.ForeignKey(default='1', to='hostess.Hostess'),
        ),
    ]
