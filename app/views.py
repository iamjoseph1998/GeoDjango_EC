from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Location
import folium
import requests

# Create your views here.
def home(request):
    if request.method == 'POST':
        city_name = request.POST['city_name']
        city_name = city_name.capitalize()
        try:
            city_data = Location.objects.get(name=city_name)
            lat = city_data.coordinates[0]
            lng = city_data.coordinates[1]

            # Temperature
            get_temp = requests.get('https://api.weather.gov/points/{lat},{lng}').json()
            print(get_temp)
            map = folium.Map(location=[lng, lat], zoom_start=6, min_zoom=3, max_zoom=18)
            folium.Marker([lng, lat], tooltip='View temperature', popup=f'{city_name} Temperature').add_to(map)
            map = map._repr_html_()
            context = {
                'map': map
            }
            return render(request, 'app/home.html', context)
        except Location.DoesNotExist:
            map = folium.Map(location=[21.0000, 78.0000], zoom_start=4, min_zoom=3, max_zoom=18)
            map = map._repr_html_()
            context = {
                'map': map
            }
            return render(request, 'app/home.html', context)
    else:
        map = folium.Map(location=[21.0000, 78.0000], zoom_start=4, min_zoom=3, max_zoom=18)
        map = map._repr_html_()
        context = {
            'map': map
        }
        return render(request, 'app/home.html', context)