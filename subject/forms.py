from django import forms
from .models import *

class ScoreForm(forms.ModelForm):
    score = forms.IntegerField(min_value=2,max_value=5)
    class Meta:
        model = Score
        fields = ['subject','pupil', 'score',]