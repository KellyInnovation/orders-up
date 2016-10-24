from django.conf.urls import include, url
from rest_framework import routers

from guest.viewsets import GuestViewSet
from hostess.viewsets import HostessViewSet
from kitchen.viewsets import KitchenViewSet

router = routers.DefaultRouter()
router.register(r'guest', GuestViewSet)
router.register(r'hostess', HostessViewSet)
router.register(r'kitchen', KitchenViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
]