try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from PIL import Image

from django.db import models

MAX_SUBJECTS = 5

# Create your models here.
class Teacher(models.Model):
    """ Model for storing details about the teachers such as name, phone, subjects etc"""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=False, blank=True)
    profile_pic = models.ImageField(upload_to='images', default='/images/default/image.jpeg')
    email_address = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20)
    room_number = models.CharField(max_length=100)
    subject = models.TextField(max_length=500, help_text='Enter a comma separated list of subjects, max 5')

    def __str__(self):
        return self.email_address


    def save(self, *args, **kwargs):

        if not self.id and not self.profile_pic:
            return

        # restrict subjects to 5
        if self.subject:
            self.subject = ','.join(self.subject.split(',')[:MAX_SUBJECTS])
              
        # resizing the image to 100, 100 so it can display properly on profile page
        image = Image.open(self.profile_pic)

        image.thumbnail((100, 100))
        image.save(self.profile_pic.path)
        super(Teacher, self).save(*args, **kwargs)



