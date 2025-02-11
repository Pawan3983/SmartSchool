from django.shortcuts import render, get_object_or_404
from .models import Subject, Attendance

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject/subject_list.html', {'subjects': subjects})

def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    return render(request, 'subject/subject_detail.html', {'subject': subject})

def attendance_report(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    attendance = subject.attendances.all()
    return render(request, 'subject/attendance_report.html', {'subject': subject, 'attendance': attendance})
