from django.shortcuts import render, redirect
from . import forms
from task.models import Task

# Create your views here.
def add_task(request):
    task_form = forms.TaskForm()
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')
        
    return render(request, 'add_task.html', {"form" : task_form})

def edit_task(request, id):
    task = Task.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')
        
    return render(request, 'add_task.html', {"form" : task_form})

def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('show_tasks')