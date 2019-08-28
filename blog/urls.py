from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('bookreview.html', views.bookreview, name='testing'),
    path('test/', views.test, name='test'),
] 

