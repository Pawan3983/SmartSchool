from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),  # Display list of students
    path('<int:student_id>/', views.student_detail, name='student_detail'),  # Student details
    path('add/', views.add_student, name='add_student'),
]
