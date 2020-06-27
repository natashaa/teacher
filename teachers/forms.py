from django import forms
from string import Template
from django.utils.safestring import mark_safe

from .models import Teacher, MAX_SUBJECTS

# Create the form class.

class TeacherForm(forms.ModelForm):
    """ Form for validating the techer record """

    def clean_subject(self):
        subjects = self.cleaned_data['subject']
        if len(list(filter(None, subjects.split(',')))) > MAX_SUBJECTS:
            raise forms.ValidationError("The maximum number of subjects can't be more than {}".format(MAX_SUBJECTS))

        subjects = ','.join(list(filter(None, subjects.split(','))))
        return subjects
    
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email_address', 'phone', 'profile_pic', 'room_number', 'subject']


class ImportForm(forms.Form):
    """ form for importing csv file for teacher records and zip for teacher images """

    csv_file = forms.FileField(label='CSV File Path', allow_empty_file=False)
    images_zip_file = forms.FileField(label='Images Zip File Path', allow_empty_file=False)