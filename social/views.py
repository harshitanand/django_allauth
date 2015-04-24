from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'index.html')
def feature(request):
    return render(request, 'base.html')
def profile(request):
    return render(request, 'profile.html')