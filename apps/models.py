from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

STATUS = {
    'student':'student',
    'teacher':'teacher'
}

class User(AbstractUser):
    bio = models.TextField(max_length=300, blank=True)
    profile_picture = models.URLField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    status = models.CharField(max_length=300,choices = STATUS ,null=True)

    def __str__(self):
        return self.username

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    content = models.TextField()
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order}. {self.title} - {self.course.title}"

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"




