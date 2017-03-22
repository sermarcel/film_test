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


class Movie(models.Model):
    title = models.CharField(max_length=64)
    rating = models.IntegerField(choices=RANK_CHOICE, default=-1)
    genere = models.IntegerField(choices=GENERE, default=-1)

# Create your models here.
