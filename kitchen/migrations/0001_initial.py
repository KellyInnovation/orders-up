# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.TextField(null=True, blank=True)),
                ('item_price', models.DecimalField(max_digits=1000, decimal_places=0)),
                ('meat_size', models.CharField(max_length=20, null=True, blank=True)),
                ('category', models.CharField(max_length=100, default='Other', null=True, blank=True, choices=[('APPETIZERS', 'Appetizers'), ('SALADS', 'Salads and Soups'), ('BEEF', 'Beef'), ('SEAFOOD', 'Seafood'), ('POULTRY', 'Poultry'), ('PORK', 'Pork'), ('PASTA', 'Pastas'), ('DRINKS', 'Drinks'), ('SIDES', 'Side Items'), ('DESSERTS', 'Desserts'), ('OTHER', 'Other')])),
                ('guest', models.ForeignKey(null=True, to='guest.Guest', blank=True, related_name='guest_menu')),
            ],
        ),
    ]
