from django.db import models

from party.models import Party

class Hostess(models.Model):
	SEATING_CHOICES = (
		('ANY', 'Any'),
		('BOOTH', 'Booth'),
		('TABLE', 'Table'),
	)

	checkin_time = models.DateTimeField(auto_now_add=True)
	# checkin_time = models.DurationField(default=timedelta(minutes=30))


	party_name = models.CharField(max_length=200)
	number_in_party = models.IntegerField()
	phone_number = models.CharField(max_length=200)
	
	seating = models.CharField(max_length=100, choices=SEATING_CHOICES, default='Any')
	seating_requests = models.TextField(max_length=500, null=True, blank=True)

	def save(self, *args, **kwargs):

		super().save(*args, **kwargs)
		party, created = Party.objects.get_or_create(hostess=self)

	#slug = models.SlugField()

	# def create_party_id(self, party_name, id):
	# 	party_concat = "{}-{}".format(self.party_name, self.pk)

	# 	party_id = self.create(party_concat=party_concat)

	# 	return party_id
