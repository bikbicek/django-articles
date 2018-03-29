from django.urls import path
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.articles, name='index'),
    path('kategorie/<str:category>/', views.articles, name='category'),
    path('region/<str:region>/', views.articles, name='region'),
    path('clanek/<int:id>/', views.article, name='article'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
