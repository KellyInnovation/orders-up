# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0001_initial'),
        ('kitchen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KitchenOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('time_ordered', models.DateTimeField(auto_now_add=True)),
                ('kitchen', models.ForeignKey(to='kitchen.Kitchen')),
                ('party', models.ForeignKey(to='party.Party')),
            ],
        ),
    ]
