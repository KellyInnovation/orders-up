from django.db import models

class Guest(models.Model):

	first_name = models.CharField(max_length=70, null=True, blank=True)
	last_name = models.CharField(max_length=70, null=True, blank=True)

	party_number = models.IntegerField()
	party_url = models.CharField(max_length=300)

	drink = models.CharField(max_length=30, default='water')
	appetizer = models.CharField(max_length=100, null=True, blank=True)
	entree = models.CharField(max_length=50, null=True, blank=True)
	side_item = models.CharField(max_length=100, null=True, blank=True)
	dessert = models.CharField(max_length=100, null=True, blank=True)

	special_instructions = models.CharField(max_length=500, null=True, blank=True)
