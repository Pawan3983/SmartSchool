from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from subject.models import Attendance, Subject
from student.models import Student

def teacher_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'teacher/login.html', {'error': 'Invalid credentials'})
    return render(request, 'teacher/login.html')

@login_required
def dashboard(request):
    subjects = Subject.objects.filter(teachers__user=request.user)
    return render(request, 'teacher/dashboard.html', {'subjects': subjects})

@login_required
def mark_attendance(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    students = Student.objects.all()
    if request.method == 'POST':
        for student in students:
            is_present = request.POST.get(f'present_{student.id}', 'off') == 'on'
            Attendance.objects.create(student=student, subject=subject, is_present=is_present)
        return redirect('dashboard')
    return render(request, 'teacher/mark_attendance.html', {'students': students, 'subject': subject})

def teacher_logout(request):
    logout(request)
    return redirect('login')
