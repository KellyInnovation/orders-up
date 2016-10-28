from rest_framework import serializers

from .models import PartyOrder, GuestOrder

class GuestOrderSerializer(serializers.ModelSerializer):

	class Meta:
		model = GuestOrder
		fields = ('id', 'drink', 'food', 'special_instructions',)

class PartyOrderSerializer(serializers.ModelSerializer):
	guest_user = GuestOrderSerializer(many=True)	

	class Meta: 
		model = PartyOrder
		fields = ('id', 'guest_user',)

