from django.db import models

class Kitchen(models.Model):

	menu_item_name = models.CharField(max_length=200)
	menu_item_description = models.TextField(null=True, blank=True)
	menu_item_price = models.DecimalField(max_digits=10000, decimal_places=2)

	meat_size = models.CharField(max_length=20, null=True, blank=True)
