from django.shortcuts import render

# Create your views here.

def home(request):
    d = {'Author' : 'Naeem', 'age' : 5, 'course' : [
        {
            'id' : 1,
            'name' : 'C++',
            'fee' : 1000
        },
        {
            'id' : 2,
            'name' : 'Python',
            'fee' : 4000
        },
        {
            'id' : 3,
            'name' : 'Django',
            'fee' : 5000
        }
    ]}
    return render(request, 'first_app/home.html', d)
