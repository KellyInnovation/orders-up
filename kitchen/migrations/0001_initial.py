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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.TextField(blank=True, null=True)),
                ('item_price', models.DecimalField(max_digits=1000, decimal_places=0)),
                ('meat_size', models.CharField(blank=True, max_length=20, null=True)),
                ('category', models.CharField(default='Other', choices=[('APPETIZERS', 'Appetizers'), ('SALADS', 'Salads and Soups'), ('BEEF', 'Beef'), ('SEAFOOD', 'Seafood'), ('POULTRY', 'Poultry'), ('PORK', 'Pork'), ('PASTA', 'Pastas'), ('DRINKS', 'Drinks'), ('SIDES', 'Side Items'), ('DESSERTS', 'Desserts'), ('OTHER', 'Other')], blank=True, max_length=100, null=True)),
            ],
        ),
    ]
