from django.db import models

class Movie(models.Model):
    name = models.TextField(default='')
    detail = models.TextField(default='')
    release_date = models.TextField(default='')
    rate = models.FloatField(default=0)
    viewer = models.IntegerField(default=0)
    poster = models.URLField(default='')
    add_date = models.TextField(default='')
