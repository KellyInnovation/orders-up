# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0006_auto_20161024_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kitchen',
            old_name='menu_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='kitchen',
            old_name='menu_item_description',
            new_name='item_description',
        ),
        migrations.RenameField(
            model_name='kitchen',
            old_name='menu_item_name',
            new_name='item_name',
        ),
        migrations.RenameField(
            model_name='kitchen',
            old_name='menu_item_price',
            new_name='item_price',
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='guest_order',
            field=models.ForeignKey(blank=True, to='guest.GuestOrder', null=True),
        ),
    ]
