# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0006_auto_20161026_1732'),
        ('kitchen', '0007_auto_20161026_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitchen',
            name='guest_order',
        ),
        migrations.AddField(
            model_name='kitchen',
            name='guest',
            field=models.ForeignKey(blank=True, to='guest.Guest', null=True, related_name='guest_menu'),
        ),
    ]
