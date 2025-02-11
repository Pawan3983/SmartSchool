from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject_list, name='subject_list'),  # Display list of subjects
    path('<int:subject_id>/', views.subject_detail, name='subject_detail'),  # Subject details
    path('<int:subject_id>/attendance/', views.attendance_report, name='attendance_report'),  # Attendance for a subject
]
