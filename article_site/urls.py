from django.urls import path

from . import views

urlpatterns = [
    path('', views.articles, name='index'),
    path('<str:category>/', views.articles, name='category'),
    path('clanek/<int:id>/', views.article, name='article'),
]