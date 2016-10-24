from rest_framework import serializers

from .models import Kitchen

class KitchenSerializer(serializers.ModelSerializer):

	class Meta:
		model = Kitchen
		fields = ('id', 'menu_item_name', 'menu_item_description', 'menu_item_price', 'meat_size', 'menu_category',)