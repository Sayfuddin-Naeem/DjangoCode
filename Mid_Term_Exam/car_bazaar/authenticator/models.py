from django.db import models
from cars.models import Car
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class OrderHistory(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    car = models.ForeignKey(Car, verbose_name=_("Purchased Car"), on_delete=models.CASCADE)
    purchased_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"User: {self.user.first_name}, Car: {self.car.title}"