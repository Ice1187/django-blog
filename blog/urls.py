from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('bookreviews.html', views.bookreviews, name='bookreviews'),
    path('writeups/', views.writeups, name='writeups'),
    path('test/', views.test, name='test'),
] 

