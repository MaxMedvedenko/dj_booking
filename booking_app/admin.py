from django.contrib import admin
from booking_app.models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Room)
admin.site.register(Booking)