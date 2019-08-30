from django.db import models

# Create your models here.

class WriteupCTF(models.Model):
	name = models.CharField(default='Unknow', max_length=50)
	date = models.DateField()
	img = models.ImageField(upload_to='writeup/', blank=True)
	team = models.CharField(max_length=255, default='Ice1187')
	rank = models.CharField(max_length=10, blank=True)
	score = models.IntegerField(default=0)
	trashtalk = models.TextField(blank=True)

	class Meta():
		ordering = ["-date", "name"]
		get_latest_by = "-date"

	def __str__(self):
		return self.name


class WriteupCategory(models.Model):
	name = models.CharField(default='Uncategorized', max_length=50)

	def __str__(self):
		return self.name


class WriteupArticle(models.Model):
	ctf = models.ForeignKey('WriteupCTF', default='Unknow', on_delete=models.SET_DEFAULT)
	category = models.ForeignKey('WriteupCategory', default='Uncategorize', on_delete=models.SET_DEFAULT,)
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	hint = models.TextField(blank=True)
	solution = models.TextField()
	tags = models.ManyToManyField('WriteupTag', blank=True)

	class Meta():
		ordering = ["category", "name"]

	def __str__(self):
		return self.name


class WriteupTag(models.Model):
	name = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.name

class ReviewArticle(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateField()
	img = models.ImageField(upload_to='review/', blank=True)
	author = models.TextField()
	about = models.TextField(blank=True)
	review = models.TextField()

	class Meta():
		ordering = ["-date", "name"]
		get_latest_by = "-date"

	def __str__(self):
		return self.name



