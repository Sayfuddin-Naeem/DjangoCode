from django.db import models
from taskCategory.models import Category
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField(default=timezone.now().date())
    task_category = models.ManyToManyField(Category)
    
    def __str__(self) -> str:
        return self.task_title