from django.shortcuts import render
from .models import Article, Category

def articles(request, category = None):
	if category:
		cur = Category.objects.filter(name=category)[0]
		return render(request, "articles.html", {"articles": Article.objects.filter(category=cur)})
	else:
		return render(request, "articles.html", {"articles": Article.objects.all()})


def article(request, id):
	return render(request, "article.html", {"article": Article.objects.get(id=id)})