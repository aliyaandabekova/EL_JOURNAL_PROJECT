from django.urls import path
from .views import *

urlpatterns = [
    path('pupils/<int:subject_id>/',pupil_page,name='pupils'),
    path('pupils_detail/',pupils_detail,name='pupils_detail'),
    path('pupil_detail/<int:pupil_id>/',pupil_detail,name='pupil_detail'),

]