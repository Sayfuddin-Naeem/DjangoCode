from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from cars.models import Car
from authenticator.models import OrderHistory
from comments.forms import CommentForm

# Create your views here.

class CarDetailView(DetailView):
    model = Car
    pk_url_kwarg = 'car_id'
    template_name = 'car_details.html'
    
    def post(self, request, *args, **kwargs):
        car = self.get_object()
        comment_form = CommentForm(data = self.request.POST)
        if comment_form.is_valid():
            comment_form.instance.car = car
            comment_form.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = CommentForm()
        
        context['car'] = car
        context['comments'] = comments
        context['comment_form'] = comment_form
        
        return context
    
class PurchasedCarDetailView(DetailView):
    model = OrderHistory
    pk_url_kwarg = 'order_id'
    template_name = 'purchased_car_details.html'
    context_object_name = 'order'