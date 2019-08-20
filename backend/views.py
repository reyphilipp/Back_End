from rest_framework import viewsets
from .models import Address
from backend.serializers import AddressSerializer


class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()