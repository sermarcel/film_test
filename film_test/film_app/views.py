from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from film_app.models import Movie

# Create your views here.
class AddMovie (CreateView):
    model = Movie
    fields = '__all__'
    template_name = '/add_movie.html'
