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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('time_ordered', models.DateTimeField(auto_now_add=True)),
                ('kitchen', models.ForeignKey(to='kitchen.Kitchen')),
                ('party', models.ForeignKey(to='party.Party')),
            ],
        ),
    ]
