import csv
import json
import os
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from zipfile import ZipFile
from PIL import Image

from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from .models import Teacher
from .forms import TeacherForm, ImportForm


def index(request):
    """ Index page for all teachers, shows all teachers available in a school """

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
    """ Detail view for a teacher, displays details like name, phone, email, subject etc """

    teacher = get_object_or_404(Teacher, pk=teacher_id)
    form = TeacherForm(instance=teacher)
    return render(request, 'teachers/detail.html', {'form': form})


@login_required
def importer(request):
    """ File importer for saving teachers in bulk """
    
    error = None
    if request.method == 'POST':
        import_form = ImportForm(request.POST, request.FILES)
        if import_form.is_valid():
            input_zip = request.FILES['images_zip_file']
            try:
                with ZipFile(input_zip, 'r') as zip_ref:
                    for entry in zip_ref.infolist():
                        with zip_ref.open(entry) as file:
                            image = Image.open(file)
                            image.thumbnail((100, 100))
                            image.save('{}/images/{}'.format(settings.MEDIA_ROOT, entry.filename))
            except:
                # Log the error
                error = 'There is a problem with images zip file, try again with another zip file.'
                print(error)
            else:
                try:
                    csv_file = request.FILES['csv_file'].read().decode('utf-8')
                except UnicodeDecodeError:
                    # log it
                    error = 'There is some problem with csv file that you are using, try again with another csv file.'
                    print(error)
                else:
                    csv_data = csv.DictReader(StringIO(csv_file), delimiter=',')
                    for row in csv_data:
                        # CSV headers - First Name,Last Name,Profile picture,Email Address,Phone Number,Room Number,Subjects taught
                        data_dict = {
                            'first_name': row['First Name'],
                            'last_name': row['Last Name'],
                            'email_address': row['Email Address'],
                            'phone': row['Phone Number'],
                            'room_number': row['Room Number'],
                            'subject': row['Subjects taught'],
                            'profile_pic': 'images/{}'.format(row['Profile picture'])
                        }
                        if not row['Email Address']:
                            # TODO: log it
                            print('No unique key, email address available')
                            continue
                        profile_pic_path = '{}/{}'.format(settings.MEDIA_ROOT, data_dict.get('profile_pic'))
                        if not os.path.isfile(profile_pic_path):
                            data_dict['profile_pic'] = 'images/dummy.jpeg'
                        try:
                            teacher = Teacher.objects.get(email_address=data_dict.get('email_address'))
                        except Teacher.DoesNotExist:
                            Teacher.objects.create(**data_dict)
                        else:
                            # Not using quesryset update as model save() doesn't get called which has the logic
                            # for limit subjects to 5
                            for (key, value) in data_dict.items():
                                setattr(teacher, key, value)
                                teacher.save()
                    
                    return HttpResponseRedirect(reverse('import_success'))
    else:
        import_form = ImportForm()
        

    return render(request, 'teachers/importer.html', {'import_form': import_form, 'error': error})


def import_success(request):
    template = 'teachers/import_success.html'
    context = {}
    return render(request, template, context)




