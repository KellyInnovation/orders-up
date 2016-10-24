# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hostess',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('unique_party_id', models.IntegerField(default=1)),
                ('unique_party_url', models.URLField(blank=True)),
                ('party_name', models.CharField(max_length=200)),
                ('number_in_party', models.IntegerField()),
                ('phone_number', models.CharField(max_length=200)),
                ('seating', models.CharField(default='Any', max_length=100, choices=[('ANY', 'Any'), ('BOOTH', 'Booth'), ('TABLE', 'Table')])),
                ('seating_requests', models.CharField(max_length=500)),
            ],
        ),
    ]
