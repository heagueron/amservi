from rest_framework import serializers
from services.models import ServiceType, Order

from django.contrib.auth.models import User

class ServiceTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceType
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.username')

    class Meta:
        model = Order
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    orders_as_client = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())
    orders_as_provider = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username')
        fields = ('id', 'username', 'orders_as_client', 'orders_as_provider')

# In a query to UserSerializer would appear 
# the user as provider or client.