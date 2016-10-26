# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0004_auto_20161026_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('drink', models.CharField(max_length=30, default='water')),
                ('food', models.CharField(max_length=400, null=True, blank=True)),
                ('special_instructions', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='guest',
            name='appetizer',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='dessert',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='drink',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='entree',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='side_item',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='special_instructions',
        ),
        migrations.AddField(
            model_name='guestorder',
            name='guest',
            field=models.ForeignKey(to='guest.Guest', related_name='guest_order'),
        ),
    ]
