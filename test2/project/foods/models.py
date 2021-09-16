from django.db import models


# Create your models here.

class Food (models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(max_length=3)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)