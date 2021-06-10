from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Subject(models.Model):
    title = models.CharField(max_length=30)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Score(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True)
    pupil = models.ForeignKey("Pupil", on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)


class Pupil(models.Model):
    name = models.CharField(max_length=30,default='Алия')
    subject = models.ManyToManyField(Subject)
    avg_score = models.FloatField(default=0)
    photo = models.ImageField()
    def __str__(self):
        return self.name






