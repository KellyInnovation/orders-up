from rest_framework import serializers

from .models import GuestOrder, Party

class GuestOrderSerializer(serializers.ModelSerializer):

	class Meta:
		model = GuestOrder
		fields = ('id', 'drink', 'food', 'special_instructions',)

class PartySerializer(serializers.ModelSerializer):

	class Meta:
		model = Party
		fields = ('id', 'drink', 'food', 'special_instructions',)