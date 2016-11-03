# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0002_auto_20161102_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, default=1, auto_created=True, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='party',
            name='hostess',
            field=models.OneToOneField(to='hostess.Hostess'),
        ),
    ]
