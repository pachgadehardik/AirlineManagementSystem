from django.db import models
import datetime
from django.contrib.auth.models import User



# Create your models here.
class Check(models.Model):
    source = models.CharField(max_length = 30)
    destination = models.CharField(max_length = 30)
    cost = models.IntegerField()
     
    def __str__(self):
        return self.source+' '+self.destination
         
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length = 30)
    source = models.CharField(max_length = 30)
    destination = models.CharField(max_length = 30)  
    date = models.DateField(("Date"))
    tclass = models.CharField(max_length = 30)
    flight = models.CharField(max_length = 30)

    def __str__(self):
        return self.name



