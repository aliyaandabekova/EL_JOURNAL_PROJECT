from django.contrib import admin
from .models import *

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title','teacher']
admin.site.register(Subject,SubjectAdmin)


class ScoreAdmin(admin.ModelAdmin):
    list_display = ['subject','pupil','score']
admin.site.register(Score,ScoreAdmin)

