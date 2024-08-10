from django.urls import path
from first_app.views import *

urlpatterns = [
    path('', set_session, name='home'),
    path('get_cookies/', get_cookies, name='get_cookies'),
    path('get_sessions/', get_session, name='get_sessions'),
    # path('delete_cookies/', del_cookies, name='delete'),
    path('delete_sessions/', del_sessions, name='delete'),
]
