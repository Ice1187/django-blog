from django.urls import path, re_path, include
from . import views

app_name = 'blog'
urlpatterns = [
	path('', views.redirect_to_index),
    path('index.html', views.index, name='index'),
    path('writeups/', views.writeups, name='writeups'),
    path('writeups/<slug:ctfname>/', views.ctf, name='ctf'),
    path('writeups/<slug:ctfname>/<str:problemname>', views.problem, name='problem'),
    path('bookreviews.html', views.bookreviews, name='bookreviews'),
    path('test/', views.test, name='test'),
    re_path(r'^markdownx/', include('markdownx.urls')),
] 
