import datetime as dt
from django.shortcuts import render, redirect
from django.template import loader, Context
from .models import WriteupCategory, WriteupArticle, WriteupCTF, WriteupTag, ReviewArticle


def redirect_to_index(request):
	return redirect('blog:index')

def index(request):
	writeups = WriteupArticle.objects.select_related('ctf')
	writeupimg = WriteupCTF.objects.latest().img
	reviews = ReviewArticle.objects.all()
	reviewimg = ReviewArticle.objects.latest().img
	var = {
		'writeups': writeups[:4],
		'reviews': reviews[:4],
		'reviewimg': reviewimg,
		'writeupimg':  writeupimg,
		}
	return render(request, 'blog/index.html', var)


def writeups(request):
	writeups = WriteupArticle.objects.select_related('ctf')
	ctfs = WriteupCTF.objects.all()
	var = {
		'writeups': writeups[:8],
		'ctfs': ctfs[:3],
	}
	return render(request, 'blog/writeups.html', var)


def ctf(request, ctfname):
	ctf = WriteupCTF.objects.get(name=ctfname)
	articles = ctf.writeuparticle_set.order_by('category__name')
	categories = { 'Rev': [], 'Pwn': [], 'Web': [], 'Crypto': [], 'Forensic': [], 'Misc': []}
	for article in articles:
		category = article.category.name
		if category not in categories.keys():
			categories.update(dict(category, []))
		categories[category].append(article)
	var = {
		'ctf': ctf, 
		'categories': categories,
	}
	return render(request, 'blog/ctf.html', var)


def problem(request, ctfname, problemname):
	ctf = WriteupCTF.objects.get(name=ctfname)
	problem = WriteupArticle.objects.select_related('ctf')
	problem = problem.get(ctf__name=ctfname, name=problemname)
	var = {
		'ctf': ctf,
		'problem': problem,
	}
	return render(request, 'blog/problem.html', var)


def bookreviews(request):
    return render(request, 'blog/bookreviews.html')


def test(request):
    return render(request, 'blog/test.html', {'datetime': dt.datetime.now()})
