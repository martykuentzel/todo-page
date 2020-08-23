from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import TaskForm
from .models import Task

def index(request):
    task_list = Task.objects.all()
    context = {'task_list': task_list}
    print(task_list)
    return render(request, 'task/index.html', context)

# Create your views here.
def create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            print("Task saved")
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()

    return render(request, 'task/create.html', {'form': form})

def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return HttpResponseRedirect('/')