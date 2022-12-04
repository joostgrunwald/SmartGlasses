from django.urls import path
from . import views
from medicines.views import medicinesListView
app_name = 'medicines'

urlpatterns = [
    #path('medicines', views.medicinesView, name = 'medicines'),
    path("medicines/", medicinesListView.as_view()),
    path('medicines/add', views.addView, name='add'),
]

#https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html