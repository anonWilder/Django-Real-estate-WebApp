from django.shortcuts import render
from .models import *
from .models import BlogPost
#def index(request):
 #   return render(request,'index.html')



def index(request):
    posts = BlogPost.objects.all()
    video_blogs = VideoBlog.objects.all()
    context = {'posts': posts, 'video_blogs': video_blogs}
    return render(request, 'index.html', context)



def about(request):
    return render(request,'about-us.html')


def contact(request):
    return render(request,'contact-us.html')


def download(request):
    return render(request,'downloads.html')


def schedule_inspection(request):
    return render(request,'schedule-inspection.html')

def our_projects(request):
    return render(request,'our-projects.html')
