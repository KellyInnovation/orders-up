from django.db import models
# from django.template.defaultfilters import slugify

class Hostess(models.Model):
	SEATING_CHOICES = (
		('ANY', 'Any'),
		('BOOTH', 'Booth'),
		('TABLE', 'Table'),
	)

	# hostess_slug = models.SlugField(unique=True, blank=True,)
	# unique_party_url = models.URLField(blank=True)
	checkin_time = models.DateTimeField(auto_now_add=True)

	party_name = models.CharField(max_length=200)
	number_in_party = models.IntegerField()
	phone_number = models.CharField(max_length=200)
	
	seating = models.CharField(max_length=100, choices=SEATING_CHOICES, default='Any')
	seating_requests = models.TextField(max_length=500, null=True, blank=True)

