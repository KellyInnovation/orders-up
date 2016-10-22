from rest_framework import viewsets

from .models import Guest
from .serializers import GuestSerializer

class GuestViewSet(viewsets.ModelViewSet):

	queryset = Guest.objects.all().order_by('-party_number')
	serializer_class = GuestSerializer