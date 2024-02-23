from django.urls import path
from booking_app.views import *
urlpatterns = [
    path('', index, name = "index"),
]