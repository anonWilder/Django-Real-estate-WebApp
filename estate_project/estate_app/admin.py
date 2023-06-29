from django.contrib import admin
from .models import BlogPost
from .models import VideoBlog
from .models import NumberBlock
from .models import Project
from .models import Download
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(VideoBlog)
admin.site.register(NumberBlock)
admin.site.register(Project)
admin.site.register(Download)
