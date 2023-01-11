from django.shortcuts import render
from medicines.forms import MedicineForm
from django.shortcuts import render, redirect
from .models import Medicine

def addView(request):
    args = {}
    if request.POST:
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicines:medicine_list')
    else:
        form = MedicineForm()
    args['form'] = form
    return render(request, 'medicines/add.html', args)


def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request,'medicines/medicines.html', {'medicines':medicines})

def medicine_edit(request, pk):
    medicine = Medicine.objects.get(pk=pk)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicines:medicine_list')
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'medicines/medicine_edit.html', {'form': form, 'medicine': medicine})

def medicine_delete(request, pk):
    medicine = Medicine.objects.get(pk = pk)
    if request.method == 'POST':
        medicine.delete()
        return redirect('medicines:medicine_list')
    return render(request, 'medicines/medicine_delete.html', {'medicine':medicine})