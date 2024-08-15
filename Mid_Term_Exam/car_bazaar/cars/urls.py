from django.urls import path
from cars.views import *

urlpatterns = [
    path('details/<int:car_id>', CarDetailView.as_view(), name='car_detail'),
    path('purchased/details/<int:order_id>', PurchasedCarDetailView.as_view(), name='purchased_car_detail'),
]
