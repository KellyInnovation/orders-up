from rest_framework import viewsets

from .models import Hostess
from .serializers import HostessSerializer

class HostessViewSet(viewsets.ModelViewSet):
	queryset = Hostess.objects.all()
	serializer_class = HostessSerializer