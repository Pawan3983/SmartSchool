from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.teacher_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('mark-attendance/<int:subject_id>/', views.mark_attendance, name='mark_attendance'),
    path('logout/', views.teacher_logout, name='logout'),
]
