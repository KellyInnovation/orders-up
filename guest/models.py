from django.db import models

class Guest(models.Model):

	first_name = models.CharField(max_length=70, null=True, blank=True)
	last_name = models.CharField(max_length=70, null=True, blank=True)

	party_url = models.ForeignKey('hostess.Hostess', default='1')

	food_options = models.ForeignKey('kitchen.Kitchen', null=True, blank=True, related_name='menu_options')

class GuestOrder(models.Model):

	drink = models.CharField(max_length=30, default='water')
	food = models.CharField(max_length=400, null=True, blank=True)

	special_instructions = models.CharField(max_length=500, null=True, blank=True)	

	guest = models.ForeignKey(Guest, related_name='guest_order')