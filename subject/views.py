from django.shortcuts import render,redirect
from .models import *
from .forms import ScoreForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
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
        return redirect('home')
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('home')

def score_page(request,pupil_id,subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
    except Subject.DoesNotExist:
        return HttpResponse('Авторизуйтесь или у вас нет урока по указанному id')
    try:
        pupil = Pupil.objects.get(id=pupil_id)
    except Pupil.DoesNotExist:
        return HttpResponse('Ученика по указанным id нет')
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









