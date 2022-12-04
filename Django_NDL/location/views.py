from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
import geopy.distance
# Create your views here.

def locationView(request):
    g = GeoIP2()
   # ip = get_client_ip(request) Woudl usually do this, but takes loopback now which doesnt work
    coords_cur = g.lat_lon('google.com')
    coords_home = ('51.82546', '5.86894')
    distance = geopy.distance.geodesic(coords_home, coords_cur).km
    return render(request, 'location/location.html',{
        'distance' : distance,
        'coords_cur' : coords_cur,
    })
    

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
