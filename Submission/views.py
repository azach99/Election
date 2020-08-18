from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'Submission/home.html')

@login_required
def profile(request):
    return render(request, 'Submission/profile.html')
