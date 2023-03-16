from django.contrib import admin
from .models import Student,Faculty,Task
# Register your models here.
@admin.register(Student)

class StudentModelAdmin(admin.ModelAdmin):
    list_display=['student_name','rollno','standard']

@admin.register(Faculty)

class FacultyModelAdmin(admin.ModelAdmin):
    list_display=['Faculty_name','standard','student_name']  

@admin.register(Task)

class TaskModelAdmin(admin.ModelAdmin):
    list_display=['task_name','description', 'student_name', 'Faculty_name', 'start_time','end_time','status']

    
