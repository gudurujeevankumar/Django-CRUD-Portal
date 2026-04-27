from enum import unique
from django.db import models

# Create your models here.
class Sdetails(models.Model):
    roll_no = models.CharField(max_length=10,unique = True)
    st_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(unique = True)
    branch = models.CharField(max_length=30)

    def __str__(self):
        return self.st_name
    
