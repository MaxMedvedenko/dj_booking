from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CustomUser(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    patronymic = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Room(models.Model):
    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=100)
    capacity = models.IntegerField()
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    
    user_email = models.EmailField()
    telefon = models.CharField(max_length=15, null=True, blank=True)
    
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
