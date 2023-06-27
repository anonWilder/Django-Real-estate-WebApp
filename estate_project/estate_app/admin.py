from django.contrib import admin
from .models import BlogPost
from .models import VideoBlog

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(VideoBlog)