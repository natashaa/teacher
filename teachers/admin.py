from django.contrib import admin

from .models import Teacher
from .forms import TeacherForm

class TeacherAdmin(admin.ModelAdmin):
    form = TeacherForm

admin.site.register(Teacher, TeacherAdmin)