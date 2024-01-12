from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypis_eshop, name='vypis-eshop'),
    path('kategoria/', views.vypis_kategorie, name='vypis-kategorie'),
    path('produkt/', views.vypis_produkt, name='vypis-produkt'),
    path('uzivatel/', views.vypis_uzivatela, name='vypis-uzivatela'),
    path('objednavka/', views.vypis_objednavka, name = 'vypis-objednavka')
]