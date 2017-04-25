from django.db import models
from datetime import datetime
from django.core import serializers


class Movie(models.Model):
    name = models.TextField(default='')
    detail = models.TextField(default='')
    lead_actors = models.TextField(default='')
    director = models.TextField(default='')
    genre = models.TextField(default='')
    release_date = models.TextField(default='')
    rate = models.FloatField(default=0)
    viewer = models.IntegerField(default=0)
    poster = models.URLField(default='')
    add_date = models.DateTimeField(default=datetime.now, blank=True)
    countcom = models.IntegerField(default=0)
    clip = models.TextField(default='')



class Comment(models.Model):
    movie = models.ForeignKey(Movie, default=None)
    user = models.TextField(default='')
    comment_text = models.TextField(default='')
    date = models.DateTimeField(default=datetime.now, blank=True)
    like = models.IntegerField(default=0)


def Movie_xml():
    XMLSerializer = serializers.get_serializer("xml")
    xml_serializer = XMLSerializer()
    with open("MovieRate/file.xml", "w") as out:
        xml_serializer.serialize(Movie.objects.all(), stream=out)
