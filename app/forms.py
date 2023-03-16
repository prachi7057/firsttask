from django import forms
from.models import *
from django.contrib.admin.widgets import AdminSplitDateTime

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model= Student
        fields= ['student_name','rollno','standard']
        widgets = {'student_name':forms.TextInput(attrs={'class':'form-control'}),
                   'rollno':forms.TextInput(attrs={'class':'form-control'}),
                   'standard':forms.TextInput(attrs={'class':'form-control'}),
                   }
        
class FacultyRegistrationForm(forms.ModelForm):
    class Meta:
        model= Faculty
        fields= ['Faculty_name','standard','student_name']
        widgets = {'Faculty_name':forms.TextInput(attrs={'class':'form-control'}),
                   'standard':forms.TextInput(attrs={'class':'form-control'}),
                   'student_name':forms.Select(attrs={'class':'form-control'}),
                   }        
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['student_name'].queryset = Faculty.objects.none()  

# class DateForm(forms.ModelForm):
#      class Meta:
#         model= Task
#         fields= ['task_name','description', 'student_name', 'Faculty_name', 'start_time','end_time','status']
#         start_date = forms.DateTimeField(
#         input_formats=['%d/%m/%Y %H:%M'],
#         widget=forms.DateTimeInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })
#     )
#         end_date = forms.DateTimeField(
#         input_formats=['%d/%m/%Y %H:%M'],
#         widget=forms.DateTimeInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })
#     )

class TaskAsignForm(forms.ModelForm):
    start_time=forms.SplitDateTimeField(widget=AdminSplitDateTime())
    end_time=forms.SplitDateTimeField(widget=AdminSplitDateTime())

    class Meta:
        model= Task
        fields= '__all__'
        
    
       
             