# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestorder',
            name='party',
            field=models.ForeignKey(related_name='guest_user', default=1234, to='party_order.PartyOrder'),
            preserve_default=False,
        ),
    ]
