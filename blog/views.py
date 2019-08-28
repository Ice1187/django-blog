import datetime as dt
from django.shortcuts import render
from django.template import loader, Context
from .models import WriteupCategory, WriteupArticle, WriteupCTF, WriteupTag, ReviewArticle



def index(request):
	writeups = WriteupArticle.objects.select_related('ctf')
	writeupimg = WriteupCTF.objects.get(pk=1).img
	reviews = ReviewArticle.objects.all()
	reviewimg = ReviewArticle.objects.get(pk=1).img
	img = {
		'writeups': writeups,
		'reviews': reviews,
		'reviewimg': reviewimg,
		'writeupimg':  writeupimg,
		}
	return render(request, 'blog/index.html', img)


def bookreview(request):
    return render(request, 'blog/bookreview.html')


def test(request):
    return render(request, 'blog/test.html', {'datetime': dt.datetime.now()})
