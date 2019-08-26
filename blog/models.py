from django.db import models

# Create your models here.

class WriteupArticle(models.Model):
	ctf = models.ForeignKey('WriteupCTF', on_delete=models.SET_DEFAULT, default='Unknow')
	category = models.ForeignKey('WriteupCategory', on_delete=models.SET_DEFAULT, default='Uncategorize')
	title = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	hint = models.TextField(blank=True)
	solution = models.TextField()
	tags = models.ManyToManyField('WriteupTag')

	def __str__(self):
		return self.title


class WriteupCategory(models.Model):
	name = models.CharField(default='Uncategorized', max_length=50)

	def __str__(self):
		return self.name


class WriteupCTF(models.Model):
	name = models.CharField(default='Unknow', max_length=50)
	date = models.DateField()

	def __str__(self):
		return self.name


class WriteupTag(models.Model):
	name = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.name