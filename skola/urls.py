from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypis_skola, name='skola'),
    path('triedy/', views.vypis_triedy, name='triedy'),
    path('ucitelia/', views.vypis_ucitela, name='ucitelia'),
    path('studenti/', views.vypis_studenta, name='studenti'),
    path("triedy/<trieda>/", views.vypis_trieda, name='trieda'),
]