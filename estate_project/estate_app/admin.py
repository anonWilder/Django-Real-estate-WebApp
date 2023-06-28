from django.contrib import admin
from .models import BlogPost
from .models import VideoBlog
from .models import NumberBlock
from .models import Project
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(VideoBlog)
admin.site.register(NumberBlock)
admin.site.register(Project)

