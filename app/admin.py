from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Location

# Register your models here.
class LocationAdmin(LeafletGeoAdmin):
    list_display = ('name', 'coordinates',)
    search_fields = ('name',)

admin.site.register(Location, LocationAdmin)