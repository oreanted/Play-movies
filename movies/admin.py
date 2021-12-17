from django.contrib import admin
from .models import Movie, Genre, Payment


# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('title', 'release_year', 'movie_rate', 'genre')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("costumer_name", "email", "address", "card_holder", "card_number", "cash")


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Payment, PaymentAdmin)
