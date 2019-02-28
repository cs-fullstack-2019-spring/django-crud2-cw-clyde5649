from django.db import models

# Create your models here.


class Person(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=40)
    phonenumber = models.IntegerField(max_length=10)
