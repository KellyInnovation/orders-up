from django.db import models

class Hostess(models.Model):
	SEATING_CHOICES = (
		('ANY', 'Any'),
		('BOOTH', 'Booth'),
		('TABLE', 'Table'),
	)

	unique_party_id = models.IntegerField(default=1)
	unique_party_url = models.URLField(blank=True)

	party_name = models.CharField(max_length=200)
	number_in_party = models.IntegerField()
	phone_number = models.CharField(max_length=200)
	
	seating = models.CharField(max_length=100, choices=SEATING_CHOICES, default='Any')
	seating_requests = models.CharField(max_length=500, null=True, blank=True)