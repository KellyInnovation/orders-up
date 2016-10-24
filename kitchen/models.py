from django.db import models

class Kitchen(models.Model):
	CATEGORY_CHOICES = (
		('APPETIZERS', 'Appetizers'),
		('SALADS', 'Salads and Soups'),
		('BEEF', 'Beef'),
		('SEAFOOD', 'Seafood'),
		('POULTRY', 'Poultry'),
		('PORK', 'Pork'),
		('PASTA', 'Pastas'), 
		('DRINKS', 'Drinks'),
		('SIDES', 'Side Items'),
		('DESSERTS', 'Desserts'),
		('OTHER', 'Other'),
	)


	menu_item_name = models.CharField(max_length=200)
	menu_item_description = models.TextField(null=True, blank=True)
	menu_item_price = models.DecimalField(max_digits=10000, decimal_places=2)

	meat_size = models.CharField(max_length=20, null=True, blank=True)
	menu_category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Other', null=True, blank=True)

