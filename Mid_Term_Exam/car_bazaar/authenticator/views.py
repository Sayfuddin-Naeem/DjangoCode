from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from authenticator.forms import RegisterForm, MyPasswordChangeForm, ChangeUserDataForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.models import User
from cars.models import Car
from authenticator.models import OrderHistory
from django.views.generic import UpdateView, CreateView, View, ListView
    
class SignupFormView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'user_form.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('login')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('profile'))
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Account Created Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Account Information Incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["heading"] = "Sign Up Page"
        context["type"] = "Sign Up"
        return context
    
    
class UserLoginView(LoginView):
    template_name = 'user_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('profile'))
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self) -> str:
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Logged in information incorrect')
        return response
    
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["heading"] = "Login Page"
        context["type"] = "Login"
        return context

@method_decorator(login_required, name='dispatch')
class ProfileView(ListView):
     model = OrderHistory
     template_name = 'profile.html'
     context_object_name = 'orders'
     
     def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    
    
@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    model = User
    form_class = ChangeUserDataForm
    template_name = 'update_profile.html'
    success_url  = reverse_lazy('profile')
    
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Account Updated Successfully')
        return super().form_valid(form)
    

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Logged Out Successfully')
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class UserPassChangeView(PasswordChangeView):
    form_class = MyPasswordChangeForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Password changed successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Enter Correct Password Format')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["heading"] = "Change Your Password"
        context["type"] = "Change Password"
        return context

@method_decorator(login_required, name='dispatch')    
class BuyNowView(View):
    def post(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        
        if car.quantity > 0:
            car.quantity -= 1
            car.save()
            
            OrderHistory.objects.create(car=car, user=request.user)
            
            messages.success(request, 'Car purchased successfully!')
        else:
            messages.error(request, 'Sorry, this car is out of stock.')

        return redirect('home')