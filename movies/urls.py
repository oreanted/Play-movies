from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drama/', views.genre_drama, name='drama'),
    path('action/', views.genre_action, name='action'),
    path('adventure/', views.genre_adventure, name='adventure'),
    path('comedy/', views.genre_comedy, name='comedy'),
    path('romance/', views.genre_romance, name='romance'),
    path('indian_cinema/', views.genre_indian_cinema, name='indian'),
    path('si-fi/', views.genre_science, name='fiction'),
    path('payment/', views.payment, name='pay')
]
