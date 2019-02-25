from rest_framework import generics

from services.models import ServiceType
from services.serializers import ServiceTypeSerializer


class ServiceTypeListCreate(generics.ListCreateAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer

"""
By taking a look at the generic API views documentation we can 
see that there’s a view for listing and creating models.

It’s ListCreateAPIView.

The ListCreateAPIView takes a queryset and a serializer_class.
"""
