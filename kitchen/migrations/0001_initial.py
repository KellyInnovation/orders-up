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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.TextField(blank=True, null=True)),
                ('item_price', models.DecimalField(decimal_places=0, max_digits=1000)),
                ('meat_size', models.CharField(max_length=20, blank=True, null=True)),
                ('category', models.CharField(choices=[('APPETIZERS', 'Appetizers'), ('SALADS', 'Salads and Soups'), ('BEEF', 'Beef'), ('SEAFOOD', 'Seafood'), ('POULTRY', 'Poultry'), ('PORK', 'Pork'), ('PASTA', 'Pastas'), ('DRINKS', 'Drinks'), ('SIDES', 'Side Items'), ('DESSERTS', 'Desserts'), ('OTHER', 'Other')], null=True, max_length=100, blank=True, default='Other')),
            ],
        ),
    ]
