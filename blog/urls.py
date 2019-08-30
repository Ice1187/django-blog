from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('writeups/', views.writeups, name='writeups'),
    path('writeups/<slug:ctfname>/', views.ctf, name='ctf'),
    path('bookreviews.html', views.bookreviews, name='bookreviews'),
    path('test/', views.test, name='test'),
] 

