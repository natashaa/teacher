try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from PIL import Image

from django.db import models

MAX_SUBJECTS = 5

# Create your models here.
class Teacher(models.Model):
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
            
        super(Teacher, self).save(*args, **kwargs)

        if not self.id and not self.profile_pic:
            return           

        super(Teacher, self).save(*args, **kwargs)

        image = Image.open(self.profile_pic)

        image.thumbnail((100, 100))
        image.save(self.profile_pic.path)



