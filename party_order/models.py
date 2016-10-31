from django.db import models

class PartyOrder(models.Model):

	hostess_party = models.ForeignKey('hostess.Hostess', related_name='hostess_party')

	drink = models.CharField(max_length=30, default='water')
	food = models.CharField(max_length=400, null=True, blank=True)

	special_instructions = models.CharField(max_length=500, null=True, blank=True)	


class GuestOrder(models.Model):

	drink = models.CharField(max_length=30, default='water')
	food = models.CharField(max_length=400, null=True, blank=True)

	special_instructions = models.CharField(max_length=500, null=True, blank=True)	

	guest = models.ForeignKey('guest.Guest', related_name='guest_order')
	party = models.ForeignKey(PartyOrder, related_name='guest_user')