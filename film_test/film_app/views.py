from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from film_app.models import Movie
import requests

# Create your views here.
class AddMovie (CreateView):
    model = Movie
    fields = '__all__'
    template_name = '/add_movie.html'

class SearchMovie(models.Model):

    parameters ={'api_key':'}
    # open the url and the screen name 
    # (The screen name is the screen name of the user for whom to return results for)#
    #response = requests.get( "https://api.themoviedb.org/3/movie", params=parameters)
    id=5
    response = requests.get( 'https://api.themoviedb.org/3/movie/{}'.format(id), params=parameters)

    data = response.json()


    # print the result
    print (data)
