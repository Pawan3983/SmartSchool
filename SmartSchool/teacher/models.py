from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # OneToOne with User model
    subject = models.ManyToManyField('subject.Subject', related_name='teachers')  # ManyToMany with Subject

    def __str__(self):
        return self.user.username

