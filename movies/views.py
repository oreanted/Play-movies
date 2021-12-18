from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie, Genre, Payment
from .forms import PaymentForm
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request,):
    movies = Movie.objects.filter()
    genres = Genre.objects.all()
    return render(request, 'index.html', {'movies': movies, "genres": genres})


def genre_drama(request, ):
    drama = Movie.objects.filter(genre=7)
    return render(request, 'drama.html', {'drama': drama})


def genre_action(request):
    action = Movie.objects.filter(genre=1)
    return render(request, 'action.html', {'action': action})


def genre_adventure(request):
    adventure = Movie.objects.filter(genre=2)
    return render(request, 'adventure.html', {'movie_adv': adventure})


def genre_comedy(request):
    comedy = Movie.objects.filter(genre=3)
    return render(request, 'comedy.html', {'comedy': comedy})


def genre_romance(request):
    romance = Movie.objects.filter(genre=5)
    return render(request, 'romance.html', {'romance': romance})


def genre_indian_cinema(request):
    indian_cinema = Movie.objects.filter(genre=9)
    return render(request, 'indian_cinema.html', {'cinema': indian_cinema})


def genre_science(request):
    science = Movie.objects.filter(genre=5)
    return render(request, 'science_fiction.html', {'science': science})


@login_required()
def payment(request):
    if request.method == "POST":
        pay = PaymentForm(request.POST or None)
        if pay.is_valid():
            pay.save()
        return redirect('pay')
    else:

        return render(request, 'payment.html')
