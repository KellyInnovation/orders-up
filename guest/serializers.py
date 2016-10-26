from rest_framework import serializers

from .models import Guest, GuestOrder

from kitchen.serializers import KitchenSerializer

class GuestOrderSerializer(serializers.ModelSerializer):

	class Meta:
		model = GuestOrder
		fields = ('id', 'drink', 'food', 'special_instructions',)

class GuestSerializer(serializers.ModelSerializer):
	guest_order = GuestOrderSerializer(many=True)
	guest_menu = KitchenSerializer(many=True, read_only=True)


	class Meta:
		model = Guest
		fields = ('id', 'first_name', 'last_name', 'party_id', 'guest_order', 'guest_menu',)

