from rest_framework import viewsets

from .models import Kitchen
from .serializers import KitchenSerializer

class KitchenViewSet(viewsets.ModelViewSet):
	queryset = Kitchen.objects.all()
	serializer_class = KitchenSerializer