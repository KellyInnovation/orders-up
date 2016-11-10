# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='hostess',
            field=models.OneToOneField(blank=True, null=True, to='hostess.Hostess'),
        ),
    ]
