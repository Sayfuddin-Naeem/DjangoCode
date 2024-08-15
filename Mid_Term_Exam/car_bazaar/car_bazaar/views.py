from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from cars.models import Car
from brands.models import Brand
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.contrib import messages    

class HomeView(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset()
        brand_slug = self.kwargs.get('brand_slug')
        if brand_slug:
            brand = get_object_or_404(Brand, slug=brand_slug)
            queryset = queryset.filter(brand=brand)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        context['slBrand'] = None
        brand_slug = self.kwargs.get('brand_slug')
        if brand_slug:
            context['slBrand'] = get_object_or_404(Brand, slug=brand_slug)
        return context