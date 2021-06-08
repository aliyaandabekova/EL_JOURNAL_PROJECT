from django import forms
from .models import *

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['subject','pupil', 'score']