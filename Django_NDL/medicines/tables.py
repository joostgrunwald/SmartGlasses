import django_tables2 as tables
from .models import Medicine
'''
class MedicineTable(tables.Table):
    class Meta:
        model = Medicine
        template_name = "django_tables2/bootstrap.html"
        row_attrs = {
        "onClick": lambda record: "document.location.href='/app/view/{0}';".format(record.id)
    }
        fields  = ("name","amount",)
'''
#https://www.youtube.com/watch?v=jCM-m_3Ysqk&ab_channel=Codemy.com
#Currently using a different method