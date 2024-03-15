from django.db import models

class CustomUser(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    
    user_id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=50, default='') 
    name = models.CharField(max_length=50, default='')
    surname = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')
    
    def __str__(self):
        return f"{self.name} {self.surname}"


class Room(models.Model):
    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=100)
    capacity = models.IntegerField()
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    check_in_date = models.DateField()
    check_out_date = models.DateField()