from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypis_posty, name='vypis-posty'),
    path('autors/', views.vypis_autorov, name='vypis-autorov'),
    path('categories/', views.vypis_kategorie, name='vypis-kategorie'),
]