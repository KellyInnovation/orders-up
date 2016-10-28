from django.db import models

class Guest(models.Model):

	first_name = models.CharField(max_length=70, null=True, blank=True)
	last_name = models.CharField(max_length=70, null=True, blank=True)

	party_url = models.ForeignKey('hostess.Hostess', default='1')
