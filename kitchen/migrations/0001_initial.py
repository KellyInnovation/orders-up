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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.TextField(blank=True, null=True)),
                ('item_price', models.DecimalField(max_digits=1000, decimal_places=0)),
                ('meat_size', models.CharField(blank=True, null=True, max_length=20)),
                ('category', models.CharField(choices=[('APPETIZERS', 'Appetizers'), ('SALADS', 'Salads and Soups'), ('BEEF', 'Beef'), ('SEAFOOD', 'Seafood'), ('POULTRY', 'Poultry'), ('PORK', 'Pork'), ('PASTA', 'Pastas'), ('DRINKS', 'Drinks'), ('SIDES', 'Side Items'), ('DESSERTS', 'Desserts'), ('OTHER', 'Other')], blank=True, null=True, max_length=100, default='Other')),
            ],
        ),
    ]
