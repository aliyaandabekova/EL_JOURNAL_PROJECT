from django.contrib import admin
from .models import *
# Register your models here.

class PupilAdmin(admin.ModelAdmin):
    list_display = ['name', 'avg_score']
admin.site.register(Pupil,PupilAdmin)
