from django import forms
from django.forms import ModelForm
from MovieRate.models import Movie


class MovieForm(ModelForm):

    class Meta:
        model = Movie

        fields=['name','detail','release_date','rate','viewer','poster','add_date']



