from django.urls import path
from posts.views import *

urlpatterns = [
    # path('add/', add_blog, name='add_blog'),
    path('add/', AddBlogtCreateView.as_view(), name='add_blog'),
    # path('edit/<int:id>', edit_blog, name='edit_blog'),
    path('edit/<int:id>', EditBlogView.as_view(), name='edit_blog'),
    # path('delete/<int:id>', delete_blog, name='delete_blog'),
    path('delete/<int:id>', DeleteBlogView.as_view(), name='delete_blog'),
    path('details/<int:id>', BlogDetailView.as_view(), name='detail_blog'),
]