from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Subject(models.Model):
    title = models.CharField(max_length=30)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)


class Score(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    pupil = models.CharField(max_length=20,default='Ученик')
    score = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)


