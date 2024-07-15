from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This is home page from second app.")
def courses(request):
    return HttpResponse("This is course page from second app.")
def about(request):
    return HttpResponse("This is about page from second app.")
