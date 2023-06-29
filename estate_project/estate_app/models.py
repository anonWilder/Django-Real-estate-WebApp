from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400, default='')
    content = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=100)
    comments = models.IntegerField()

    def __str__(self):
        return self.title

class VideoBlog(models.Model):
    youtube_url = models.URLField()

    # Add any additional fields as needed

    def __str__(self):
        return self.youtube_url

class NumberBlock(models.Model):
    image = models.ImageField(upload_to='number_blocks')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_images/')
    description = models.TextField()

    def __str__(self):
        return self.title



class Download(models.Model):
    name = models.CharField(max_length=255, default='')
    link = models.URLField(default='')

    def __str__(self):
        return self.name
