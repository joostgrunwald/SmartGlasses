from selenium import webdriver
from geopy.geocoders import Nominatim
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import geopy.distance
import time
import datetime

away = False
maxDistance = 4

def getLocation():
    RecentlyCalled = False
    while not RecentlyCalled:
        # Create a timer that calls the script every 5 minutes
        timer = datetime.datetime.now()
        print(timer)
        timer = timer + datetime.timedelta(minutes=5)
        print(timer)
        while(datetime.datetime.now() < timer):
            i = 3
            # we wait


        print("we zijn er")
        options = Options()
        options.add_argument("--use-fake-ui-for-media-stream")
        timeout = 20
        driver = webdriver.Chrome(
        executable_path='./chromedriver.exe', chrome_options=options)
        driver.get("https://mycurrentlocation.net/")
        wait = WebDriverWait(driver, timeout)
        time.sleep(3)
        longitude = driver.find_elements("xpath", '//*[@id="longitude"]')
        longitude = [x.text for x in longitude]
        longitude = str(longitude[0])
        latitude = driver.find_elements("xpath", '//*[@id="latitude"]')
        latitude = [x.text for x in latitude]
        latitude = str(latitude[0])
        driver.quit()

        latitude_home = '51.82546'
        longitude_home = '5.86894'
        coords_home = (latitude_home, longitude_home)
        coords_cur = (latitude, longitude)
        distance = geopy.distance.geodesic(coords_home, coords_cur).km
        print(distance)
        if (distance > maxDistance):
            print("oma is weg")
            RecentlyCalled = True
            # bericht sturen
            # iets met counter
        else:
            print("oma is thuis")

            # bericht sturen
            # counter resetten


def mainfunc():
    while True:
        #call once every 30 minutes
        currentTime = datetime.datetime.now()
        currentTime = currentTime + datetime.timedelta(minutes=30)
        while datetime.datetime.now() < currentTime:
            getLocation()

if __name__ == "__main__":
    mainfunc()

#https://sites.google.com/a/chromium.org/chromedriver/downloads
#https://codeburst.io/how-i-understood-getting-accurate-geolocation-using-python-web-scraping-and-selenium-7967d721587a
#('51.82546', '5.86894')
