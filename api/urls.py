from django.conf.urls import include, url
from rest_framework import routers

from guest.viewsets import GuestViewSet

router = routers.DefaultRouter()
router.register(r'guest', GuestViewSet)


urlpatterns = [
	url(r'^', include(router.urls)),
]