from django.shortcuts import render
from . forms import ContactForm, StudentForm, PasswordValidationProject
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    user = None
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        select = request.POST.get('select')
        
        user = {'name' : name, 'email' : email, 'select' : select}
        return render(request, 'about.html', {'user' : user})
    else:
        return render(request, 'about.html')

def form(request):
    return render(request, 'form.html')

def django_form(request):
    if request.method == 'POST':
        formData = ContactForm(request.POST, request.FILES)
        if formData.is_valid():
            # file = formData.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            return render(request, 'django_form.html', {'form' : formData})
    
    else:
        formData = ContactForm()
    return render(request, 'django_form.html', {'form' : formData})

def student_form(request):
    if request.method == 'POST':
        formData = StudentForm(request.POST, request.FILES)
        return render(request, 'django_form.html', {'form' : formData})
    
    else:
        formData = StudentForm()
        return render(request, 'django_form.html', {'form' : formData})
    
def PasswordValidation(request):
    if request.method == 'POST':
        formData = PasswordValidationProject(request.POST)
        return render(request, 'django_form.html', {'form' : formData})
    
    else:
        formData = PasswordValidationProject()
        return render(request, 'django_form.html', {'form' : formData})
        