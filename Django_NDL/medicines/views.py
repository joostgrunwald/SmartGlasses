from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
import geopy.distance
# Create your views here.

def medicinesView(request):
    preScript = [("Azithromycin", 3),("Metformin", 2),("Lisinopril", 2)]
    times = ["08:00", "20:00"]
    context = {
        'times' : times,
        'preScript' : preScript
    }
    return render(request, 'medicines/medicines.html', context)
