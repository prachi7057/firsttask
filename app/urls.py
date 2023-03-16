from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
from django.views.i18n import JavaScriptCatalog
urlpatterns = [
    path('jsi18n',JavaScriptCatalog.as_view(),name='js-catlog'),
    path('',views.student,name='studentform'),
    path('studentlist/',views.stulist,name='studentlist'),
    path('facultyform/',views.faculty,name='facultyform'),
    path('facultylist/',views.faculty_list,name='facultylist'),
    path('taskform/',views.add_task,name='taskform'),
    path('task_list',views.task_list,name='task'),
    path('task_details/<int:faculty_id>',views.task_details,name='taskdetails'),
    path('completetask/<int:task_id>',views.complete_task,name='taskcomplete'),
    path('search/',views.search),



]   