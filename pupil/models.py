from django.db import models
from subject.models import *

# Create your models here.


class Pupil(models.Model):
    name = models.CharField(max_length=30,default='Ученик')
    subject = models.ManyToManyField(Subject)
    avg_score = models.FloatField()
