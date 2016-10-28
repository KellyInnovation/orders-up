from django.conf.urls import include, url
from rest_framework import routers

from guest.viewsets import GuestViewSet
from hostess.viewsets import HostessViewSet
from kitchen.viewsets import KitchenViewSet
from party_order.viewsets import PartyOrderViewSet

router = routers.DefaultRouter()
router.register(r'guest', GuestViewSet)
router.register(r'hostess', HostessViewSet)
router.register(r'kitchen', KitchenViewSet)
router.register(r'party', PartyOrderViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
]