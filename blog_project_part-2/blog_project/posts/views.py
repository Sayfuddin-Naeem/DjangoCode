from django.shortcuts import render, redirect
from . import forms
from posts.models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_blog(request):
    blog_form = forms.PostForm()
    if request.method == 'POST':
        blog_form = forms.PostForm(request.POST)
        if blog_form.is_valid():
            blog_form.instance.author = request.user
            blog_form.save()
            messages.success(request, 'Blog added successfully !!')
            return redirect('add_blog')
        
    return render(request, 'add_blog.html', {"form" : blog_form, 'type' : 'Add Blog'})

@login_required
def edit_blog(request, id):
    blog = Post.objects.get(pk=id)
    blog_form = forms.PostForm(instance=blog)
    if request.method == 'POST':
        blog_form = forms.PostForm(request.POST, instance=blog)
        if blog_form.is_valid():
            blog_form.instance.author = request.user
            blog_form.save()
            return redirect('home')
        
    return render(request, 'add_blog.html', {"form" : blog_form, 'type' : 'Edit Blog'})

@login_required
def delete_blog(request, id):
    blog = Post.objects.get(pk=id)
    blog.delete()
    return redirect('profile')