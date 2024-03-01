from django.shortcuts import render
from booking_app.models import *

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# Create your views here.

def index(request):
    room = Room.objects.all()
    content = {'rooms': room}
    return render(request, 'booking_app/index.html', content)

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