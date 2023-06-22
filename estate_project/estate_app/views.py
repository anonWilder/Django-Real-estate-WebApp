from django.shortcuts import render
from .models import *

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about-us.html')


def contact(request):
    return render(request,'contact-us.html')


def download(request):
    return render(request,'downloads.html')


def apointment(request):
    return render(request,'schedule-inspection.html')
