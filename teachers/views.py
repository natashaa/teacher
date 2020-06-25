from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Teacher
from .forms import TeacherForm


def index(request):
    teachers = Teacher.objects.all()
    if request.method == 'GET':
        last_name_letter = request.GET.get('last_name_letter')
        subjects = request.GET.get('subject_s')
        if last_name_letter:
            teachers = teachers.filter(last_name__startswith=last_name_letter)
        if subjects:
            teachers = teachers.filter(subject__contains=subjects)    

    context = {
        'teachers': teachers,
    }
    return render(request, 'teachers/index.html', context)

def detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    form = TeacherForm(instance=teacher)
    return render(request, 'teachers/detail.html', {'form': form})