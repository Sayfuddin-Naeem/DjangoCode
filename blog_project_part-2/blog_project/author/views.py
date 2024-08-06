from django.shortcuts import render, redirect
from author.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from posts.models import Post

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

@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data' : data})

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
    return redirect('login')