# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0001_initial'),
        ('kitchen', '0005_kitchen_guest_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitchen',
            name='guest_order',
        ),
        migrations.AddField(
            model_name='kitchen',
            name='guest_order',
            field=models.ForeignKey(blank=True, null=True, to='guest.Guest'),
        ),
    ]
