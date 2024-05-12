from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), primary_key = True ,on_delete= models.CASCADE)
    phone_number = PhoneNumberField(null = False, blank = True, unique = True)
    