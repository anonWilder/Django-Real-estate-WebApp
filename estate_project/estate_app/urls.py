from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about, name='about-us'),
    path('contact-us/', views.contact, name='contact-us'),
    path('downloads/', views.download, name='downloads'),
    path('schedule-inspection/', views.schedule_inspection, name='schedule-inspection'),
    path('our-projects/', views.our_projects, name='our-projects'),
    path('blog/<int:post_id>/', views.blog_post, name='blog_post'),

]