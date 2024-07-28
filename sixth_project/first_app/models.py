from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    email = models.EmailField(default='example@gmail.com')
    
    def __str__(self) -> str:
        return f"{self.roll} - {self.name}"