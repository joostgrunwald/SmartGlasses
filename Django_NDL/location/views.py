from django.shortcuts import render
import geopy.distance
from django.conf import settings
from django.http import JsonResponse
import geocoder
#from twilio.rest import Client

#account_sid = 'ACb63a0a30a2dd08646e0b5397539a29ce'
#auth_token = '6c4249ef5a6007c8f18720d69b2e7105'
#client = Client(account_sid, auth_token)

coords_cur = tuple()
coords_home = (51.82546, 5.86894)


def locationView(request):
    g = geocoder
    global coords_cur
    coords_cur = (51.80, 5.86894)
    #coords_cur = g.ip('me').latlng
    #coords_cur = tuple(coords_cur)
    print(coords_cur)
    distance = geopy.distance.geodesic(coords_home[0:2], coords_cur[0:2]).km
    


    key = settings.GOOGLE_API_KEY
    return render(request, 'location/location.html',{
        'key' : key,
        'distance' : distance,
    })
    
def mydata(request):   
    global coords_home
    global coords_cur
    if (len(coords_home) < 3):
        coords_home = coords_home + ('Home',)
        coords_cur = coords_cur + ('Current',)
    '''print(coords_home)
    print(coords_cur)
    print(type(coords_home))
    print(type(coords_cur))'''
    return JsonResponse([coords_home,coords_cur], safe = False) 
