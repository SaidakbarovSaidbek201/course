from django.contrib import admin
from .models import User, Lesson, Enrollment, Course
# Register your models here.

admin.site.register(User)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Course)

