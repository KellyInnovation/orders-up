# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('menu_item_name', models.CharField(max_length=200)),
                ('menu_item_description', models.TextField(blank=True, null=True)),
                ('menu_item_price', models.DecimalField(max_digits=10000, decimal_places=2)),
            ],
        ),
    ]
