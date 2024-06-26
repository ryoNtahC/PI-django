from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypis_skola, name='skola'),
    path('triedy/', views.vypis_triedy, name='triedy'),
    path('ucitelia/', views.vypis_ucitela, name='ucitelia'),
    path('studenti/', views.vypis_studenta, name='studenti'),
    path("triedy/<trieda>/", views.vypis_trieda, name='trieda'),
    path("student/<student>/", views.vypis_student, name='student'),
    path("ucitel/<ucitel>/", views.vypis_ucitel, name='ucitel'),
    path("kruzky", views.vypis_kruzku, name='kruzky'),
    path("kruzok/<kruzok>/", views.vypis_kruzok, name='kruzok'),
    path("pridaj_uzivatel/", views.pridaj_uzivatel, name='pridaj_uzivatel'),
    path("pridaj_uzivatel2/", views.pridaj_uzivatel2, name='pridaj_uzivatel2'),

]