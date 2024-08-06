from django.urls import path
from posts.views import *

urlpatterns = [
    path('add/', add_blog, name='add_blog'),
    path('edit/<int:id>', edit_blog, name='edit_blog'),
    path('delete/<int:id>', delete_blog, name='delete_blog'),
]