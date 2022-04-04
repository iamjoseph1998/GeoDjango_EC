from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Location

# Modified Admin interface for Location
class LocationAdmin(LeafletGeoAdmin):
    list_display = ('name', 'coordinates',)
    search_fields = ('name',)

# Registered Location model to Admin panel
admin.site.register(Location, LocationAdmin)