#Django provides a default user model, but since it's somewhat limited for my needs, I’ll extend it by adding some additional fields.
#Whenever I want to override Django's default user model, I first need to create a custom model like this:

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Maculine'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True)
    phone = models.CharField(max_length=20)
 
#The code above only contains the fields I want to add, because everything else is already provided by Django's default user model.
# Now, I need to create a variable called AUTH_USER_MODEL and set it to 'app_name.CustomUser' inside the project’s settings.py file.
#After that, we move on to the form.
#(The file needs to be created.)