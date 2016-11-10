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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.TextField(null=True, blank=True)),
                ('item_price', models.DecimalField(max_digits=1000, decimal_places=0)),
                ('meat_size', models.CharField(max_length=20, null=True, blank=True)),
                ('category', models.CharField(max_length=100, null=True, choices=[('APPETIZERS', 'Appetizers'), ('SALADS', 'Salads and Soups'), ('BEEF', 'Beef'), ('SEAFOOD', 'Seafood'), ('POULTRY', 'Poultry'), ('PORK', 'Pork'), ('PASTA', 'Pastas'), ('DRINKS', 'Drinks'), ('SIDES', 'Side Items'), ('DESSERTS', 'Desserts'), ('OTHER', 'Other')], blank=True, default='Other')),
            ],
        ),
    ]
