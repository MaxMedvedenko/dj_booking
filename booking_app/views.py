from django.shortcuts import render
from booking_app.models import *

from django import forms

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
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

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'surname', 'email', 'telefon', 'check_in_date', 'check_out_date']

def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Бронювання успішно здійснено!")
        else:
            # Якщо форма недійсна, відображаємо її знову з повідомленням про помилку
            return render(request, 'booking_app/booking_form.html', {'form': form})
    else:
        form = BookingForm()
        return render(request, 'booking_app/booking_form.html', {'form': form})