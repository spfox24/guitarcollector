from django.db import models
from django.urls import reverse

class Guitar(models.Model):
    brand = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    serial = models.CharField(max_length=250)
    year = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse('guitars_detail', kwargs={'guitar_id': self.id})

class Case(models.Model):
    case = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('cases_detail', kwargs={'case_id': self.id})


