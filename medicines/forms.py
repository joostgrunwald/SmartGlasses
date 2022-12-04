from django.forms import ModelForm
from medicines.models import Medicine

class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields  = '__all__'
        