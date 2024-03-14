from django.shortcuts import render
from booking_app.models import *

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

def booking_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        telefon = request.POST.get('telefon')
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        
        # Отримання кімнати, яку бронює користувач (припустимо, що ви знаєте room_id)
        room_id = request.POST.get('room_id')
        room = Room.objects.get(pk=room_id)
        
        # Створення об'єкта Reservation з отриманими даними
        reservation = Reservation.objects.create(
            user=request.user if request.user.is_authenticated else None,
            room=room,
            start_datetime=check_in_date,
            end_datetime=check_out_date,
            user_email=email,
            telefon=telefon,
            name=name,
            surname=surname,
        ) 
        # Повернення підтвердження бронювання або перенаправлення на іншу сторінку
        return HttpResponse("Бронювання успішно здійснено!")
    else:
        return render(request, 'booking_app/booking_form.html')