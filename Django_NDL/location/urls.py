from django.urls import path
from . import views

app_name = 'location'

urlpatterns = [
    path('location/', views.locationView, name='location'),
]