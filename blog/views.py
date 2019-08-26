from django.shortcuts import render
import datetime as dt

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')


def bookreview(request):
    return render(request, 'blog/bookreview.html')


def test(request):
    return render(request, 'blog/test.html', {'datetime': dt.datetime.now()})
