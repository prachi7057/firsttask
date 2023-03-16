from django.shortcuts import render,redirect,HttpResponse
from .forms import StudentRegistrationForm,FacultyRegistrationForm,TaskAsignForm
from .models import Student,Faculty,Task
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from datetime import datetime

# Create your views here.
def student(request):
    if request.method =='POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        form = StudentRegistrationForm()
    else:
        form = StudentRegistrationForm()
    return render(request,'studentdetails.html',{'form':form})


def stulist(request):
    stu=Student.objects.all()
    return render(request,'showlist.html',{'stu': stu})


def faculty(request):

    if request.method =='POST':
        form = FacultyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        form = FacultyRegistrationForm()
    else:  
        form = FacultyRegistrationForm()
    return render(request,'facultydetail.html',{'form':form})


def faculty_list(request):
    fac=Faculty.objects.all()
    return render(request,'facultylist.html',{'fac': fac})

def add_task(request):
    if request.method == "POST":
        form = TaskAsignForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error ", form.errors)
    form = TaskAsignForm()
    return render(request, 'taskasign.html', {'form':form})

    

def task_list(request):
    tasks = Task.objects.all().order_by('start_time')
    task_name = request.GET.get('task_name')
    if task_name:
        tasks = tasks.filter(name__icontains=task_name)
    return render(request, 'tasklist.html', {'tasks': tasks})

def task_details(request, faculty_id):
    faculty = get_object_or_404(Faculty, pk=faculty_id)
    tasks = Task.objects.filter(Faculty_name=faculty)
    context = {
        'faculty': faculty,
        'tasks': tasks,
    }
    return render(request, 'taskdetails.html', context)

# def task_details(request,pk):
#     task=Task.objects.get(pk=pk)
#     faculty=Faculty.objects.all()
#     facultyname=faculty.Faculty_name
#     taskfaculty= (task.Faculty_name)
#     print(facultyname)
#     print(taskfaculty)
#     return render(request, 'taskdetails.html', {'tasks': task})

def search(request):
    query=request.GET["query"]
    var=Task.objects.filter(task_name__icontains=query)                                                  
    return render(request,"search.html",{'var':var})               


def get_time_difference(time_1, time_2):
    try:
        diff = time_1 - time_2
        days, seconds = diff.days, diff.seconds
        return {'hours' : (days * 24 + seconds // 3600), 'minutes' : ((seconds % 3600) // 60), 'seconds' : (seconds % 60)}
    except:
        return None

def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if task.status != 'COMPLETED':
        now = timezone.now()
        extra_hours = 0

        if now <= task.end_time:
            total_hours = get_time_difference(now, task.start_time)
            print(total_hours)
        else:
            total_hours = get_time_difference(task.end_time, task.start_time)
            extra_hours = get_time_difference(now, task.end_time)
            print(task.end_time)
            print( task.start_time)
        task.status = 'COMPLETED'   # the value of status is 'COMPLETED', given in caps in model
        task.save()
        context={
            'task': task,
            'total_hours': total_hours, 
            'extra_hours': extra_hours 
            }
        return render(request, 'complete_task.html',context )
    else:
        # return redirect('taskcomplete')
        return HttpResponse('Completed task not found...')
