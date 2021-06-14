from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.shortcuts import render
from subject.models import *


def pupil_page(request,subject_id):
    subjects = Subject.objects.get(id=subject_id)
    pupils = Pupil.objects.filter(subject=subjects)
    return render(request,'pupil_page.html',{'pupils':pupils, 'subject':subjects})

def pupils_detail(request):
    if isinstance(request.user,AnonymousUser):
        return HttpResponse('Вы не авторизованы!')
    subjects = Subject.objects.filter(teacher=request.user)
    pupils = Pupil.objects.filter(subject__in=subjects).distinct()
    return render(request, 'pupils_detail.html', {'pupils':pupils})

def pupil_detail(request,pupil_id):
    subjects_of_teacher = Subject.objects.filter(teacher=request.user)
    pupil = Pupil.objects.get(id=pupil_id)
    subjects_of_pupil = pupil.subject.filter(teacher=request.user)
    scores = Score.objects.filter(pupil=pupil,subject__in=subjects_of_pupil)
    return render(request,'pupil_detail.html', {'pupil':pupil,'subjects_of_pupil':subjects_of_pupil,'scores':scores})

