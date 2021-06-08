from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
# Create your views here.

def homepage(request):
    return HttpResponse('Welcome!')

def subject_page(request): # предметы авторизованного учителя
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

def score_page(request):
    form = ScoreForm()
    subjects = Subject.objects.filter(teacher=request.user)
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'score_page.html', {'form':form})


