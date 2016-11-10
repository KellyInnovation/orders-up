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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('checkin_time', models.DateTimeField(auto_now_add=True)),
                ('party_name', models.CharField(max_length=200)),
                ('number_in_party', models.IntegerField()),
                ('phone_number', models.CharField(max_length=200)),
                ('seating', models.CharField(max_length=100, choices=[('ANY', 'Any'), ('BOOTH', 'Booth'), ('TABLE', 'Table')], default='Any')),
                ('seating_requests', models.TextField(max_length=500, null=True, blank=True)),
            ],
        ),
    ]
