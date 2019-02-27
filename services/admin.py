# snippets/admin.py
from django.contrib import admin

from . models import ServiceType, Order


# Customize the way the ServiceType is presented id admin
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created')

# Customize the way the Order is presented id admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ('created', 'service_type', 'description', 'client', 'provider')

admin.site.register(ServiceType)
admin.site.register(Order)