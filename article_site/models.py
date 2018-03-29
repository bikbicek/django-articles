from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=20)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name


class Regions(models.Model):
	name = models.CharField(max_length=32)

	def __str__(self):
		return self.name


class Article(models.Model):
	header = models.CharField(max_length=64)
	main_context = models.CharField(max_length=300)
	context = models.TextField()
	date_added = models.DateTimeField(auto_now=True)
	category = models.ManyToManyField(Category)
	region = models.ForeignKey(Regions, on_delete=models.SET_NULL, null=True, blank=True)
	model_pic = models.ImageField(upload_to = 'static/articles_img/', default = 'article_site/static/img/empty.png')

	class Meta:
		ordering = ['-date_added']

	def __str__(self):
		return self.header


class Highlighted(models.Model):
	article = models.ForeignKey(Article, models.CASCADE)

	def __str__(self):
		return str(self.article)
