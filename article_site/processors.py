from .models import Category, Highlighted, Regions


def default(request):
	return {
		"categories": Category.objects.all(),
		"highlighted": Highlighted.objects.all(),
		"regions": Regions.objects.all(),
	}
