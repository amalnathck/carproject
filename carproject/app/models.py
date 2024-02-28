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
class Car(models.Model):
    company_id=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car_name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.FileField()
    model=models.CharField(max_length=100)
# class Booking(models.Model):
#     date=models.IntegerField()
