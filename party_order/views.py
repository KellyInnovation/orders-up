from django.views.generic import TemplateView

from .models import PartyOrder, GuestOrder
from .serializers import PartyOrderSerializer

class AppView(TemplateView):
	template_name = 'party/app.html'
