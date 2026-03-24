from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    msg = models.CharField(max_length=100)

def __str__(self):
    return self.name
