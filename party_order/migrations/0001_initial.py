# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostess', '0006_auto_20161026_1811'),
        ('guest', '0010_auto_20161028_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('drink', models.CharField(default='water', max_length=30)),
                ('food', models.CharField(null=True, max_length=400, blank=True)),
                ('special_instructions', models.CharField(null=True, max_length=500, blank=True)),
                ('guest', models.ForeignKey(related_name='guest_order', to='guest.Guest')),
            ],
        ),
        migrations.CreateModel(
            name='PartyOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('hostess_party', models.ForeignKey(related_name='hostess_party', to='hostess.Hostess')),
            ],
        ),
    ]
