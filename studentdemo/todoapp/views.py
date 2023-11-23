from django.http import HttpResponse
from .models import Task
from django.shortcuts import render, redirect
from .forms import TaskForm
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    # Fetch Data From Model for the current user
    tasks = Task.objects.filter(user=request.user)

    # Fetch Form from Forms
    form = TaskForm()

    # Insert Model Data into Template, Run Template Code, an Return to Client
    return render(request, 'index.html', {'tasks': tasks, 'form': form})

@login_required
def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('index')  # Redirect to wherever you want after saving