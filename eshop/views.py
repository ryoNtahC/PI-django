from django.shortcuts import render
from . models import *

def vypis_eshop(request):
    categorie = Categories.objects.all().order_by("nazov")
    produkty = Products.objects.all().order_by("nazov")
    uzivatelia = User.objects.all().order_by("username")
    objednavky = Order.objects.all()
    return render(request, "eshop/index.html", {"categorie":categorie, "produkty":produkty, "uzivatelia":uzivatelia, "objednavky":objednavky})

def vypis_kategorie(request):
    categorie = Categories.objects.all().order_by("nazov")
    return render(request, "eshop/index.html", {"categorie":categorie})

def vypis_produkt(request):
    produkty = Products.objects.all().order_by("nazov")
    return render(request, "eshop/index.html", {"produkty":produkty})

def vypis_uzivatela(request):
    uzivatelia = User.objects.all().order_by("username")
    return render(request, "eshop/index.html", {"uzivatelia":uzivatelia})

def vypis_objednavka(request):
    objednavky = Order.objects.all()
    return render(request, "eshop/index.html", {"objednavky":objednavky})