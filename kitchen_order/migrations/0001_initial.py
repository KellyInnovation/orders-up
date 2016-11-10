# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0001_initial'),
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KitchenOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('time_ordered', models.DateTimeField(auto_now_add=True)),
                ('kitchen', models.ForeignKey(to='kitchen.Kitchen')),
                ('party', models.ForeignKey(to='party.Party')),
            ],
        ),
    ]
