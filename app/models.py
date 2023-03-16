from django.db import models

# Create your models here.
class Student(models.Model):
    student_name=models.CharField(max_length=100)
    rollno=models.IntegerField()
    standard=models.IntegerField()


    def __str__(self) :
        return self.student_name    
    
class Faculty(models.Model):
    Faculty_name=models.CharField(max_length=100)
    standard=models.IntegerField()
    student_name=models.ForeignKey(Student,on_delete=models.CASCADE)

    
    def __str__(self) :
        return str(self.Faculty_name) 


class Task(models.Model):
    task_name=models.CharField(max_length=200)
    description = models.TextField()
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    Faculty_name = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    status_choices = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='PENDING')

    def __str__(self) :
        return self.student_name

    def __str__(self) :
        return str(self.Faculty_name) 
    
    # def __str__(self) :
    #     return str(self.start_time) 
    
    # def __str__(self) :
    #     return str(self.end_time)
    
    
    
