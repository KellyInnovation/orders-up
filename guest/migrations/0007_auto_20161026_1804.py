# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0006_auto_20161026_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='party_id',
            field=models.ForeignKey(related_name='guest_party', to='hostess.Hostess', default='1'),
        ),
    ]
