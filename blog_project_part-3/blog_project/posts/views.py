from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from posts.models import Post
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

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

# Add Post using class bassed view
@method_decorator(login_required, name='dispatch')
class AddBlogtCreateView(CreateView):
    model = Post
    form_class = forms.PostForm
    template_name = 'add_blog.html'
    success_url = reverse_lazy('add_blog')
    
    def form_valid(self, form) -> HttpResponse:
        form.instance.author = self.request.user
        messages.success(self.request, 'Blog added successfully !!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Add Blog'
        return context

@login_required
def edit_blog(request, id):
    blog = Post.objects.get(pk=id)
    blog_form = forms.PostForm(instance=blog)
    if request.method == 'POST':
        blog_form = forms.PostForm(request.POST, instance=blog)
        if blog_form.is_valid():
            blog_form.instance.author = request.user
            blog_form.save()
            return redirect('profile')
        
    return render(request, 'add_blog.html', {"form" : blog_form, 'type' : 'Edit Blog'})

@method_decorator(login_required, name='dispatch')
class EditBlogView(UpdateView):
    model = Post
    form_class = forms.PostForm
    template_name = 'add_blog.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Account Updated Successfully')
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Edit Blog'
        return context
    

@login_required
def delete_blog(request, id):
    blog = Post.objects.get(pk=id)
    blog.delete()
    messages.success(request, 'Blog deleted successfully')
    return redirect('profile')

@method_decorator(login_required, name='dispatch')
class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'
    
    def form_valid(self, form):
        messages.success(self.request, 'Blog deleted successfully')
        return super().form_valid(form)

# @method_decorator(login_required, name="dispatch")
class BlogDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'blog_details.html'
    
    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        comment_form = forms.CommentForm(data = self.request.POST)
        if comment_form.is_valid():
            comment_form.instance.post = blog
            comment_form.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.object
        comments = blog.comments.all()
        comment_form = forms.CommentForm()
        
        context['blog'] = blog
        context['comments'] = comments
        context['comment_form'] = comment_form
        
        return context
        
    