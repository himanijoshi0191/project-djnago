from django.urls import path
from . import views
urlpatterns = [
    path('',views.class_add,name=''),
    path('add_student/', views.add_student_data, name ='add_student')
]
