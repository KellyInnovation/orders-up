from rest_framework import serializers

from .models import Hostess

class HostessSerializer(serializers.ModelSerializer):

	party_url = serializers.HyperlinkedRelatedField(
		many=True,
		read_only=True,
		view_name='guest-detail'
	)

	class Meta:
		model = Hostess
		fields = ('id', 'party_url', 'checkin_time', 'party_name', 'number_in_party', 'phone_number', 'seating', 'seating_requests',)