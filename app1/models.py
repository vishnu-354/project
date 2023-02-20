from django.db import models

# Create your models here.
class admindb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Mobileno = models.IntegerField(null=True, blank=True)
    Username = models.CharField(max_length=100, null=True, blank=True)
    Password = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="Profile", null=True, blank=True)


class categorydb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="Profile", null=True, blank=True)


class productdb(models.Model):
    Category = models.CharField(max_length=100, null=True, blank=True)
    Productname = models.CharField(max_length=100, null=True, blank=True)
    Price = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField()
    Description = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="Profile", null=True, blank=True)

