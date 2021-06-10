from django.shortcuts import render,redirect
from .models import *
from .forms import ScoreForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from pupil.services import avg_score_count
from django.contrib.auth.models import AnonymousUser

def homepage(request):
    return render(request, 'homepage.html')

def subject_page(request): # предметы авторизованного учителя
    if isinstance(request.user,AnonymousUser):
        return HttpResponse('Вы не авторизованы!')
    else:
        subjects = Subject.objects.filter(teacher=request.user)
        # teacher = User.objects.get(id=teacher_id)
        # subjects = teacher.subject_set.all()
        return render(request, 'subject_page.html', {'subjects':subjects})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =  request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('subjects')
    return render(request, 'login.html')

def score_page(request,pupil_id,subject_id):
    subject = Subject.objects.get(id=subject_id)
    pupil = Pupil.objects.get(id=pupil_id)
    scores = pupil.score_set.all()
    print(scores)
    form = ScoreForm()
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            score = form.cleaned_data['score']
            Score.objects.create(pupil=pupil,score=score,subject=subject)
            avg_score_count(scores,pupil)
    return render(request,'score_page.html',{'pupil':pupil,'form':form})









