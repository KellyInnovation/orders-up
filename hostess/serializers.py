from rest_framework import serializers

from .models import Hostess

class HostessSerializer(serializers.ModelSerializer):


	class Meta:
		model = Hostess
		fields = ('id', 'checkin_time', 'party_name', 'number_in_party', 'phone_number', 'seating', 'seating_requests', )