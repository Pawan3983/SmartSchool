from django.db import models
from student.models import Student

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')  # OneToMany
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='attendances')  # OneToMany
    date = models.DateField(auto_now_add=True)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.date}"

