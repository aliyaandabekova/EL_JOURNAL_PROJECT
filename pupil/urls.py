from django.urls import path
from .views import *

url_patterns = [
    path('pupils/',pupil_page, name='pupils'),

]