from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=50)
    coordinates = models.PointField(srid=4326)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Location'