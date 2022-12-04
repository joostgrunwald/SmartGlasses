from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
import geopy.distance
from medicines.forms import MedicineForm
from django.shortcuts import render, HttpResponse, redirect
from .models import Medicine
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .tables import MedicineTable
# Create your views here.

def addView(request):
    args = {}
    if request.POST:
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicines:medicines')
    else:
        form = MedicineForm()
    args['form'] = form
    return render(request, 'medicines/add.html', args)

'''class medicinesView(ListView):
    model = Medicine
    template_name = 'medicines/medicines.html'
    #medicineList = Medicine.objects.all()
    #return render(request, 'medicines/medicines.html', {'medicineList' : medicineList})'''

class MedicineListView(SingleTableView):
    model = Medicine
    table_class = MedicineTable
    template_name = 'medicines/medicines.html'
