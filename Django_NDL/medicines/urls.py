from django.urls import path
from . import views

app_name = 'medicines'

urlpatterns = [
    #path('medicines', views.medicinesView, name = 'medicines'),
    path("medicines/", views.medicine_list, name = 'medicine_list'),
    path('medicines/add', views.addView, name='add'),
    path('medicines/<int:pk>/edit/', views.medicine_edit, name = 'edit'),
    path('medicines/<int:pk>/delete/', views.medicine_delete, name = 'delete'),
]

#https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html