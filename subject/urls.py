from django.urls import path
from .views import *

urlpatterns = [
    path('subjects/',subject_page, name='subjects'),
    path('scores/',score_page, name='scores'),


]