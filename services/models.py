from django.db import models


class ServiceType(models.Model):
    """
    The kind of service 
    (example: Electricidad, Plomería, Construcción, Herrería, Pintura, Jardinería)
    """
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=360, blank=True, null=True)

    def __str__(self):
        return self.title

