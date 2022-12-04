import django_tables2 as tables
from .models import Medicine

class MedicineTable(tables.Table):
    class Meta:
        model = Medicine
        template_name = "django_tables2/bootstrap.html"
        fields  = ("name","amount",)