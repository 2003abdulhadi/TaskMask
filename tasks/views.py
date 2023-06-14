from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def home(request):
    # Add any necessary logic here
    return render(request, 'tasks/home.html')