from django.db import models


RANK_CHOICE = (
    (-1, "no ranking yet"),
    (0, "*"),
    (1, "**"),
    (2, "***"),
    (3, "****"),
    (4, "*****")
)

GENERE = (
    (-1, "not defined"),
    (0, "comedy"),
    (1, "drama"),
    (2, "romance"),
    (3, "thriller"),
    (4, "horror"),
    (5, "sci-fi"),
    (6, "crime"),
    (7, "war")
    
    
)


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=64)
    rating = models.IntegerField(choices=RANK_CHOICE, default=-1)
    genere = models.IntegerField(choices=GENERE, default=-1)

class Player(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField
    famous_actor = models.ManyTo
    ocupation = models.CharField(max_length=64)
    sex = models.IntegerField(choices=SEX, default=-1)
    your_mood = models.IntegerField
    alone_or_not = 
    



class Actor(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    

