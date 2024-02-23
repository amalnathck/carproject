from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


 # Create your models here.
class CustomUser(AbstractUser):
    register_status = (
        ('approve','approve'),
        ('pending','pending'),
        ('reject','reject')
    )
    phone_number = models.IntegerField(null=True,blank=True)
    user_type = models.CharField(max_length=100,null=True,blank=True)