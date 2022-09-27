from selenium import webdriver
from geopy.geocoders import Nominatim
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import geopy.distance
import time

def getLocation():
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    driver = webdriver.Chrome(executable_path = './chromedriver.exe', chrome_options=options) #currently using 105.0.5195.52/
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)
    longitude = driver.find_elements("xpath", '//*[@id="longitude"]')  #changed this to make it compatible with current selenium version
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements("xpath", '//*[@id="latitude"]') #same change here
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    driver.quit()
    #geolocator = Nominatim(user_agent="geoapiExercises")
    #location = geolocator.reverse(latitude+","+longitude)
    #print(location)
    latitude_home = '51.82546'
    longitude_home = '5.86894'
    coords_home = (latitude_home, longitude_home)
    coords_cur = (latitude, longitude)
    print (geopy.distance.geodesic(coords_home, coords_cur).km)
    return (latitude,longitude)
print(getLocation())

#https://sites.google.com/a/chromium.org/chromedriver/downloads
#https://codeburst.io/how-i-understood-getting-accurate-geolocation-using-python-web-scraping-and-selenium-7967d721587a
#('51.82546', '5.86894')

