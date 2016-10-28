# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0009_guest_party_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestorder',
            name='guest',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='food_options',
        ),
        migrations.DeleteModel(
            name='GuestOrder',
        ),
    ]
