# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('first_name', models.CharField(blank=True, null=True, max_length=70)),
                ('last_name', models.CharField(blank=True, null=True, max_length=70)),
                ('party_url', models.ForeignKey(to='hostess.Hostess', default='1')),
            ],
        ),
    ]
