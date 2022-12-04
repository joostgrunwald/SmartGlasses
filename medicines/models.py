from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


#app_label  = 'medicines'

class Medicine(models.Model):
    name = models.CharField(max_length=50, help_text = 'Enter name of medicine')
    amount = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ],help_text = 'Enter number of times it should be taken a day')
    #times = ....

