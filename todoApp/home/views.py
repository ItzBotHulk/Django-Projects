from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Task 


# Create your views here.
def login(request):
    return render(request, 'login.html')

def home(request):
    context = {'success': False}
    # breakpoint()
    if request.method == "POST":
        #handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success':True}
        # adding task list view here 
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'index.html', context,)

def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)

def edit(request, task_id):
    # updateing the tasks 
    if request.method == "POST":
        tasks = Task.objects.get(id = task_id)
        print(tasks)
        title = request.POST['title']
        desc = request.POST['desc']
        
        tasks.taskTitle = title
        tasks.taskDesc = desc
        tasks.save()
        return redirect('')
    
    # rendering the page 
    tasks= Task.objects.get(id=task_id)      
    context = {'id': tasks.id, 'title':tasks.taskTitle, 'desc':tasks.taskDesc}
    print(context)
    return render(request, 'edit.html', context)

def delete(request):
    return render(request, 'delete.html')
    
