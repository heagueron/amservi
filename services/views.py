from rest_framework import generics, permissions
from django.contrib.auth.models import User

# to create sigle entry point to the api:
from rest_framework.decorators import api_view # new
from rest_framework.response import Response # new
from rest_framework.reverse import reverse # new

from services.models import ServiceType, Order
from services.serializers import ServiceTypeSerializer, OrderSerializer, UserSerializer
from .permissions import IsClientOrReadOnly

class ServiceTypeList(generics.ListCreateAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    
    
    def perform_create(self, serializer): # new
        serializer.save(client=self.request.user)


class ServiceTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # by overriding .perform_create() method, we can 
    # associate logged-in user that created the order (client)
    # with the order instance
    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsClientOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# For the single entry point:
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'orders': reverse('order-list', request=request, format=format)
    })


