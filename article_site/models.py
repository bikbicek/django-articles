from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=20)

	class Meta:
	        verbose_name_plural = 'Categories'

	def __str__(self):
	   return self.name

class Article(models.Model):
	header = models.CharField(max_length=64)
	main_context = models.CharField(max_length=300)
	context = models.TextField()
	date_added = models.TimeField(auto_now=True)
	category = models.ManyToManyField(Category)

	class Meta:
	        ordering = ['-date_added']

	def __str__(self):
	   return self.header
