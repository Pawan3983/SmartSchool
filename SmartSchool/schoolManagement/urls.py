from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teacher/', include('teacher.urls')),  # Teacher app
    path('students/', include('student.urls')),  # Student app
    path('subjects/', include('subject.urls')),  # Subject app
]
