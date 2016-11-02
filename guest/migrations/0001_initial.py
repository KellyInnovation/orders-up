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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70, null=True, blank=True)),
                ('last_name', models.CharField(max_length=70, null=True, blank=True)),
                ('party_url', models.ForeignKey(default='1', to='hostess.Hostess')),
            ],
        ),
    ]
