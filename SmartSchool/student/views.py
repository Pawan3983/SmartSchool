from django.shortcuts import render, get_object_or_404,redirect
from .models import Student
from .forms import StudentForm

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to the student list view
    else:
        form = StudentForm()
    return render(request, 'student/add_student.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student/student_detail.html', {'student': student})

