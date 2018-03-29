from django.shortcuts import render
from .models import Article, Category, Regions


def articles(request, category = None, region = None):

	if Article.objects.all():

		if category:
			if Category.objects.filter(name=category):
				if Article.objects.filter(category=Category.objects.filter(name=category)[0]):
					return render(request, "articles.html", {"articles": Article.objects.filter(category=Category.objects.filter(name=category)[0])})
			else:
				return render(request, "error.html", {"error_header": "Kategorie nenalezena", "error_info": "Nebylo možné najít vyhledávanou kategorii. Ověřte, zda jste správně zadali název kategorie, popřípadě nás informujte."})

		elif region:
			if Regions.objects.filter(name=region):
				if Article.objects.filter(region=Regions.objects.filter(name=region)[0]):
					return render(request, "articles.html", {"articles": Article.objects.filter(region=Regions.objects.filter(name=region)[0])})
			else:
				return render(request, "error.html", {"error_header": "Kraj nenalezen", "error_info": "Nebylo možné najít vyhledávaný kraj. Ověřte, zda jste správně zadali název kraje, popřípadě nás informujte."})

		else:
			return render(request, "articles.html", {"articles": Article.objects.all()})

	return render(request, "error.html", {"error_header": "Nebyly nalezeny žádné články", "error_info": "Nebylo možné nalézt články pro tuto sekci webu. Zkuste prosím jinou část webu, popřípadě počkejte, až se zde objeví nové články."})


def article(request, id):
	return render(request, "article.html", {"article": Article.objects.get(id=id)})
