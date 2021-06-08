from django.shortcuts import render
from .models import *
from subject.models import *
# Create your views here.

def pupil_page(request):
    if request.method == 'GET':
        subjects = Subject.objects.filter()