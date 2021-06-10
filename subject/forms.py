from django import forms
from .models import *

class ScoreForm(forms.Form):
    score = forms.IntegerField(min_value=2,max_value=5)
