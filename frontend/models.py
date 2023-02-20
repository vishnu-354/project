from django.db import models

# Create your models here.
class customerdb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    Confirmpassword = models.CharField(max_length=100, null=True, blank=True)

class contactdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)

class deliveries(models.Model):
    address = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    name = models.CharField(max_length=100,null=True, blank=True)
    qty = models.IntegerField(null=True)
    totalprice= models.IntegerField(null=True)