from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.db import models

# Location model to store city location data
class Location(models.Model):
    name = models.CharField(max_length=50)
    coordinates = models.PointField(srid=4326)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Location'