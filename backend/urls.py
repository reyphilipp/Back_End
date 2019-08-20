from django.urls import path, include
from rest_framework import routers

from backend.views import AddressView

router = routers.DefaultRouter()

router.register('addresses', AddressView, base_name='addresses')

urlpatterns = [
    path('', include(router.urls))
]