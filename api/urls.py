from django.conf.urls import include, url
from rest_framework import routers

from guest.viewsets import GuestViewSet
from hostess.viewsets import HostessViewSet

router = routers.DefaultRouter()
router.register(r'guest', GuestViewSet)
router.register(r'hostess', HostessViewSet)


urlpatterns = [
	url(r'^', include(router.urls)),
]