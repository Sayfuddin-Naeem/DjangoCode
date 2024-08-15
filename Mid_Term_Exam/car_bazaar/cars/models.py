from django.db import models
from brands.models import Brand
import os

# Create your models here.

def get_upload_to(instance, filename):
    return os.path.join('uploads', filename)

class Car(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE)
    image = models.ImageField(upload_to=get_upload_to)
    
    def __str__(self) -> str:
        return self.title