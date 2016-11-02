from django.db import models

class KitchenOrder(models.Model):
	
	kitchen = models.ForeignKey('kitchen.Kitchen')
	party = models.ForeignKey('party.Party')

	time_ordered = models.DateTimeField(auto_now_add=True)
