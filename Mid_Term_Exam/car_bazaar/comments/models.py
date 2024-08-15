from django.db import models
from cars.models import Car

# Create your models here.

class Comments(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add='True')
    
    def __str__(self) -> str:
        return f"Comment by - {self.name}"