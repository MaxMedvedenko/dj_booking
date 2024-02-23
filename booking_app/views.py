from django.shortcuts import render
from booking_app.models import *
# Create your views here.

def index(request):
    return render(request, 'booking_app/index.html')