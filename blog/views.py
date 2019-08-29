import datetime as dt
from django.shortcuts import render
from django.template import loader, Context
from .models import WriteupCategory, WriteupArticle, WriteupCTF, WriteupTag, ReviewArticle



def index(request):
	writeups = WriteupArticle.objects.select_related('ctf')
	writeupimg = WriteupCTF.objects.latest().img
	reviews = ReviewArticle.objects.all()
	reviewimg = ReviewArticle.objects.latest().img
	img = {
		'writeups': writeups[:4],
		'reviews': reviews[:4],
		'reviewimg': reviewimg,
		'writeupimg':  writeupimg,
		}
	return render(request, 'blog/index.html', img)


def writeups(request):
	writeups = WriteupArticle.objects.select_related('ctf')
	ctfs = WriteupCTF.objects.all()
	img = {
		'writeups': writeups[:8],
		'ctfs': ctfs[:3],
	}
	return render(request, 'blog/writeups.html', img)


def bookreviews(request):
    return render(request, 'blog/bookreviews.html')


def test(request):
    return render(request, 'blog/test.html', {'datetime': dt.datetime.now()})
