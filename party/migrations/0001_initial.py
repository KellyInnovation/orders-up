# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('drink', models.CharField(max_length=30, default='water')),
                ('food', models.CharField(max_length=400, null=True, blank=True)),
                ('special_instructions', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
    ]
