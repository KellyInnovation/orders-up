from rest_framework import serializers

from .models import Hostess

class HostessSerializer(serializers.ModelSerializer):

	class Meta:
		model = Hostess
		fields = ('id', 'unique_party_id', 'unique_party_url', 'checkin_time', 'party_name', 'number_in_party', 'phone_number', 'seating', 'seating_requests',)