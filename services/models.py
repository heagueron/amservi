from django.db import models


class ServiceType(models.Model):
    """
    The kind of service 
    (example: Electricidad, Plomería, Construcción, Herrería, Pintura, Jardinería)
    """
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=360, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='services', on_delete=models.CASCADE) # new
    
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

class Order(models.Model):
    """
    The instance of a service to be contracted and executed.
    """
    created = models.DateTimeField(auto_now_add=True)
    service_type = models.ForeignKey('auth.Group', related_name='service_type', on_delete=models.CASCADE)
    # service_type = models.ForeignKey('ServiceType', related_name='service_type', on_delete=models.CASCADE)
    description = models.CharField(max_length=360, blank=True, null=True)
    client = models.ForeignKey('auth.User', related_name='orders_as_client', on_delete=models.CASCADE)
    provider = models.ForeignKey('auth.User', related_name='orders_as_provider', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.description