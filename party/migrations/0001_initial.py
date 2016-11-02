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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('drink', models.CharField(max_length=30, default='water')),
                ('food', models.CharField(max_length=400, null=True, blank=True)),
                ('special_instructions', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
    ]
