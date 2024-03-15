from django.shortcuts import render, redirect
from booking_app.models import *

from django.contrib.auth import authenticate, login

from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def get_room_by_id(request, room_id):
    try:
        # Спробувати отримати кімнату за її id
        room = Room.objects.get(pk=room_id)
        
        # Якщо кімната знайдена, вивести її інформацію
        response = f"Назва кімнати: {room.name}, Тип кімнати: {room.room_type}"
        
        return HttpResponse(response)
    except Room.DoesNotExist:
        # Якщо кімната не знайдена, повернути пусту відповідь або іншу обробку за необхідності
        return HttpResponse("Кімната з вказаним ідентифікатором не знайдена")

# routes - шляхи

def index(request):
    return render(request, 'booking_app/index.html')

def room_list(request):
    rooms = Room.objects.all()
    content = {'rooms': rooms}
    print("room_list")
    print(rooms)
    return render(request, 'booking_app/room_list.html', content)

def success(request):
    return render(request, 'booking_app/success.html')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'surname', 'email', 'telefon', 'check_in_date', 'check_out_date']

def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            # Якщо форма недійсна, відображаємо її знову з повідомленням про помилку
            return render(request, 'booking_app/booking_form.html', {'form': form})
    else:
        form = BookingForm()
        return render(request, 'booking_app/booking_form.html', {'form': form})
    
    

def register_form(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Перенаправлення на сторінку успіху після успішної реєстрації
    else:
        form = CustomUserCreationForm()
    return render(request, 'register_form.html', {'form': form})

def login_form(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, nickname=nickname, email=email, password=password)
        if user is not None:
            login(request, user)
            # Перенаправлення на сторінку успіху після успішного входу
            return redirect('success')
    else:
        form = AuthenticationForm()
    return render(request, 'login_form.html', {'form': form})

