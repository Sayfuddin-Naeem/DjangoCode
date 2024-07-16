from django.shortcuts import render

def contact(request):
    return render(request, 'navigation/contact.htm')

def about(request):
    return render(request, 'navigation/about.htm')