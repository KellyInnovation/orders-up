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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.TextField(null=True, blank=True)),
                ('item_price', models.DecimalField(decimal_places=0, max_digits=1000)),
                ('meat_size', models.CharField(max_length=20, null=True, blank=True)),
                ('category', models.CharField(max_length=100, choices=[('APPETIZERS', 'Appetizers'), ('SALADS', 'Salads and Soups'), ('BEEF', 'Beef'), ('SEAFOOD', 'Seafood'), ('POULTRY', 'Poultry'), ('PORK', 'Pork'), ('PASTA', 'Pastas'), ('DRINKS', 'Drinks'), ('SIDES', 'Side Items'), ('DESSERTS', 'Desserts'), ('OTHER', 'Other')], null=True, default='Other', blank=True)),
                ('guest', models.ForeignKey(null=True, related_name='guest_menu', to='guest.Guest', blank=True)),
            ],
        ),
    ]
