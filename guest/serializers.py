from rest_framework import serializers

from .models import Guest

from kitchen.serializers import KitchenSerializer



class GuestSerializer(serializers.ModelSerializer):


	class Meta:
		model = Guest
		fields = ('id', 'first_name', 'last_name', 'party_url',)

