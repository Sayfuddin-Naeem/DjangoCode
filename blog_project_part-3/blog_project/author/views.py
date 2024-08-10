from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from author.forms import *
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from posts.models import Post
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

def signup(request):
    if not request.user.is_authenticated:
        signup_form = RegistationForm()
        if request.method == 'POST':
            signup_form = RegistationForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                messages.success(request, 'Account Created Succesfully')
                return redirect('signup')
        return render(request, 'form.html', {'form' : signup_form, 'type' : 'Sign Up'})
    else:
        return redirect('profile')

def user_login(request):
    if not request.user.is_authenticated:
        login_form = AuthenticationForm()
        if request.method == 'POST':
            login_form = AuthenticationForm(request, data = request.POST)
            if login_form.is_valid():
                name = login_form.cleaned_data['username']
                user_pass = login_form.cleaned_data['password']
                user = authenticate(username=name, password=user_pass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Succesfully')
                    return redirect('profile')
                else:
                    messages.warning(request, 'Login Information Incorrect')
                    return redirect('signup')
        return render(request, 'form.html', {'form' : login_form, 'type' : 'Login'})
    else:
        return redirect('profile')
    
class UserLoginView(LoginView):
    template_name = 'form.html'
    
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
        messages.success(self.request, 'Logged in information incorrect')
        return response
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
    

@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data' : data})

@method_decorator(login_required, name='dispatch')
class ProfileListView(ListView):
    model = Post
    template_name = 'profile.html'
    context_object_name = 'data'
    
    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.filter(author=self.request.user)

@login_required
def edit_profile(request):
    edit_form = ChangeUserDataForm(instance= request.user)
    if request.method == 'POST':
        edit_form = ChangeUserDataForm(request.POST, instance = request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Account Updated Successfully')
            return redirect('profile')
    return render(request, 'update_profile.html', {'form' : edit_form, 'type' : 'Update'})

@login_required
def change_pass(request):
    pass_form = ChangeUserPassForm(user=request.user)
    if request.method == 'POST':
        pass_form = ChangeUserPassForm(user=request.user, data=request.POST)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            messages.success(request, 'Password Changed Successfully')
            return redirect('edit_profile')
    return render(request, 'form.html', {'form' : pass_form, 'type' : 'Change Password'})

def user_logout(request):
    logout(request)
    return redirect('home')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')