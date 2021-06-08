from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def subject_page(request):
    subject = Subject.objects.all()
    return render(request, 'subject_page.html', {'subject':subject})


def score_page(request):
    form = ScoreForm(initial={'subject':request.user.subject})
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'score_page.html', {'form':form})