from selenium import webdriver
from geopy.geocoders import Nominatim
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from email.message import EmailMessage
import geopy.distance
import smtplib
import time
import datetime
import geocoder

import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

away = False
maxDistance = 4

def getLocation():
    
    RecentlyCalled = False
    while not RecentlyCalled:
        # Create a timer that calls the script every 5 minutes
        timer = datetime.datetime.now()
        print(timer)
        timer = timer + datetime.timedelta(minutes=3)
        print(timer)
        while(datetime.datetime.now() < timer):
            i = 3

        #get current latitude and longitude
        g = geocoder.ip('me')
        latitude_home = '51.82546'
        longitude_home = '5.86894'
        coords_home = (latitude_home, longitude_home)
        coords_cur = g.latlng
        print(coords_cur)
        distance = geopy.distance.geodesic(coords_home, coords_cur).km
        print(distance)
        if (distance > maxDistance):
            print("oma is weg")
            #RecentlyCalled = True
            # bericht sturen
            message = client.messages \
                .create(
                    body='Oma is kwijt and is at the following coordinates: ' + " ".join(coords_home),
                    from_='+19706327688',
                    to='+31613361986'
                )
            # iets met counterhttps://mycurrentlocation.net/
        else:
            RecentlyCalled = True
            print("oma is thuis")
            message = client.messages \
                .create(
                    body='Oma is thuis',
                    from_='+19706327688',
                    to='+31613361986'
                )
            # bericht sturen
            # counter resetten


def mainfunc():
    while True:
        #call once every 30 minutes
        currentTime = datetime.datetime.now()
        currentTime = currentTime + datetime.timedelta(minutes=15)
        while datetime.datetime.now() < currentTime:
            getLocation()

if __name__ == "__main__":
    mainfunc()

#https://sites.google.com/a/chromium.org/chromedriver/downloads
#https://codeburst.io/how-i-understood-getting-accurate-geolocation-using-python-web-scraping-and-selenium-7967d721587a
#('51.82546', '5.86894')
#Omaiskwijt0309-#