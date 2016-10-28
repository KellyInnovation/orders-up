from rest_framework import serializers

from .models import GuestOrder

class GuestOrderSerializer(serializers.ModelSerializer):

	class Meta:
		model = GuestOrder
		fields = ('id', 'drink', 'food', 'special_instructions',)