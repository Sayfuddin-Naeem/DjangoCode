from django.contrib import admin
from . import models

admin.site.register(models.Post)
admin.site.register(models.Comments)
# Register your models here.