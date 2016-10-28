from rest_framework import viewsets

from .models import GuestOrder
from .serializers import GuestOrderSerializer

class GuestOrderViewSet(viewsets.ModelViewSet):

	queryset = GuestOrder.objects.all()
	serializer_class = GuestOrderSerializer