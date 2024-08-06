from django.urls import path
from author.views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/edit/change_password/', change_pass, name='change_pass'),
    path('logout/', user_logout, name='logout'),
]