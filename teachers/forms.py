from django import forms
from string import Template
from django.utils.safestring import mark_safe

from .models import Teacher, MAX_SUBJECTS

# Create the form class.

class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html =  Template("""<img src="$link"/>""")
        if value:
            return mark_safe(html.substitute(link=value.url))
        else:
            return mark_safe(html.substitute(link=value))

class TeacherForm(forms.ModelForm):
    #profile_pic = forms.ImageField(label='Profile Pic',required=False, disabled=True)
    #profile_pic = forms.ImageField(widget=PictureWidget)

    # last_name_letter = forms.CharField(label='Last first_name', max_length=1)
    # subject_s = forms.CharField(label='Subject', max_length=1)

    def clean_subject(self):
        subjects = self.cleaned_data['subject']
        if len(list(filter(None, subjects.split(',')))) > MAX_SUBJECTS:
            raise forms.ValidationError("The maximum number of subjects can't be more than {}".format(MAX_SUBJECTS))

        subjects = ','.join(list(filter(None, subjects.split(','))))
        return subjects
    
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email_address', 'phone', 'profile_pic', 'room_number', 'subject']