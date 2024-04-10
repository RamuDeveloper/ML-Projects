from django.db import models

# Create your models here.

class Products(models.Model):
    image=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=100)
    price =models.IntegerField(default=0)
    new =models.BooleanField(default=True)
