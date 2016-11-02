from rest_framework import viewsets

from .models import KitchenOrder
from .serializers import KitchenOrderSerializer

class kitchenOrderViewSet(viewsets.ModelViewSet):
	queryset = KitchenOrder.objects.all()
	serializer_class = KitchenOrderSerializer