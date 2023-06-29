from django.shortcuts import render
from .models import *
from .models import BlogPost
from .models import Project
from .models import Download
#def index(request):
 #   return render(request,'index.html')

def index(request):
    posts = BlogPost.objects.all()
    video_blogs = VideoBlog.objects.all()
    number_blocks = NumberBlock.objects.all()
    projects = Project.objects.all()
    context = {'posts': posts, 'video_blogs': video_blogs, 'number_blocks': number_blocks, 'projects': projects}
    return render(request, 'index.html', context)


def about(request):
    number_blocks = NumberBlock.objects.all()
    context = {'number_blocks': number_blocks}
    return render(request,'about-us.html', context)


def contact(request):
    return render(request,'contact-us.html')


def download(request):
    downloads = Download.objects.all()
    return render(request, 'downloads.html', {'downloads': downloads})


def schedule_inspection(request):
    return render(request,'schedule-inspection.html')

def our_projects(request):
    return render(request,'our-projects.html')
