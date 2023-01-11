from django.urls import path
from location import views

app_name = 'location'

urlpatterns = [
    path('location/', views.locationView, name='location'),
    path('location/mydata', views.mydata, name="mydata"),
]