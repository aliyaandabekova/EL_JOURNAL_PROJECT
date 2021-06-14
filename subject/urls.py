from django.urls import path
from .views import *
from pupil.views import pupil_page


urlpatterns = [
    path('',homepage,name='home'),
    path('subjects/',subject_page, name='subjects'),
    path('login/',login_page,name='login'),
    path('scores/<int:pupil_id>/<int:subject_id>/',score_page,name='scores'),
    path('logout/',logout_page,name='logout'),

]