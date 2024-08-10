from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
import os

# Create your models here.

def get_upload_to(instance, filename):
    return os.path.join('uploads', filename)

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    image = models.ImageField(upload_to=get_upload_to, blank=True, null = True)
    
    def __str__(self) -> str:
        return self.title
    
class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add='True')
    
    def __str__(self) -> str:
        return f"Comment by - {self.name}"
    