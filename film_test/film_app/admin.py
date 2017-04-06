from django.contrib import admin
from film_app.models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name',)