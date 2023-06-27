from django.db import models

# Create your models here.

from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=100)
    comments = models.IntegerField()

    def __str__(self):
        return self.title


from django.db import models

class VideoBlog(models.Model):
    youtube_url = models.URLField()

    # Add any additional fields as needed

    def __str__(self):
        return self.youtube_url
