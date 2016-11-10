from rest_framework import serializers

from .models import Kitchen

class KitchenSerializer(serializers.ModelSerializer):

	class Meta:
		model = Kitchen
		#fields = ('id', 'item_name', 'item_description', 'item_price', 'meat_size', 'category', 'orders',)
		fields = ('id', 'item_name', 'item_description', 'item_price', 'meat_size', 'category', 'orders',)