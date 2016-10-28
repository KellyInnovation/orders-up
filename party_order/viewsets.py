from rest_framework import viewsets

from .models import PartyOrder
from .serializers import PartyOrderSerializer

class PartyOrderViewSet(viewsets.ModelViewSet):
	queryset = PartyOrder.objects.all()
	serializer_class = PartyOrderSerializer
