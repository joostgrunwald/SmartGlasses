from django.urls import path
from . import views

app_name = 'medicines'

urlpatterns = [
    path('medicines/', views.medicinesView, name='medicines'),
]