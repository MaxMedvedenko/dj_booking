from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL-шлях до головної сторінки
    # інші URL-шляхи тут
    path('rooms/', views.room_list, name='room_list'),
    path('booking_form/', views.booking_form, name='booking_form'),
]