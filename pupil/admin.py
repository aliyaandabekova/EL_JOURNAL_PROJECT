from django.contrib import admin
from subject.models import Pupil
# Register your models here.


class PupilAdmin(admin.ModelAdmin):
    list_display = ['name','avg_score']
    readonly_fields = ['avg_score']
admin.site.register(Pupil,PupilAdmin)