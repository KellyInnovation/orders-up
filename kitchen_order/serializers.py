from rest_framework import serializers

from .models import KitchenOrder

class KitchenOrderSerializer(serializers.ModelSerializer):

	class Meta:
		model = KitchenOrder
		fields = ('id', 'kitchen', 'party', 'time_ordered',)