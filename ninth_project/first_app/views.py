from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.

def home(request):
    response = render(request, 'home.html')
    # response.set_cookie('name', 'Sayfuddin', max_age=10)
    response.set_cookie('name', 'Sayfuddin', expires=datetime.now()+timedelta(days=7))
    return response

def get_cookies(request):
    name = request.COOKIES.get('name')
    return render(request, 'get_cookies.html', {'name' : name})

def del_cookies(request):
    response = render(request, 'del.html')
    response.delete_cookie('name')
    return response

def set_session(request):
    data = {
        'name' : 'Naeem',
        'age' : 28,
        'lan' : 'Bangla'
    }
    request.session.update(data)
    return render(request, 'home.html')

def get_session(request):
    request.session.get('name', 'Guest')
    data = request.session
    return render(request, 'get_sessions.html', {'data' : data})

def del_sessions(request):
    # request.session['name']
    request.session.flush()
    # request.session.delete()
    return render(request, 'del.html')
