from django.db import models

class Loc(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    latitude = models.CharField(max_length = 200, blank=True, null=True)
    longitude = models.CharField(max_length = 200, blank=True, null=True)

    def __str__(self):
        return self.name
# Create your models here.
