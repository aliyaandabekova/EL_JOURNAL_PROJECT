from django.urls import path
from .views import *

urlpatterns = [
    path('',homepage,name='home'),
    path('subjects/',subject_page, name='subjects'),
    path('scores/',score_page, name='scores'),
    path('login/',login_page,name='login')


]