from enum import unique
from django.db import models

# Create your models here.
class Ldetails(models.Model):
    l_id = models.CharField(max_length=10,unique=True)
    l_name = models.CharField(max_length=30)
    l_email = models.EmailField(unique=True)
    l_subject = models.CharField(max_length=30)

    def __str__(self):
        return self.l_name
