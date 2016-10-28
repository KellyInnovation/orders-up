from rest_framework import serializers

from .models import Guest

class GuestSerializer(serializers.ModelSerializer):


	class Meta:
		model = Guest
		fields = ('id', 'first_name', 'last_name', 'party_url',)

