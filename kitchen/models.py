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


	item_name = models.CharField(max_length=200)
	item_description = models.TextField(null=True, blank=True)
	item_price = models.DecimalField(max_digits=1000, decimal_places=0)

	meat_size = models.CharField(max_length=20, null=True, blank=True)
	category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Other', null=True, blank=True)

	# guest = models.ForeignKey('guest.Guest', null=True, blank=True, related_name='guest_menu')

	#orders = models.ManyToManyField('party.Party', through='kitchen_order.KitchenOrder', through_fields=('kitchen', 'party'))