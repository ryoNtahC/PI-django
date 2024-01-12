from django.shortcuts import render
from . models import *

def vypis_posty(request):
    posty = Post.objects.all().order_by("autor")
    return render(request, "blog/index.html", {"posty":posty})

def vypis_kategorie(request):
    categorie = Categories.objects.all().order_by("nazov")
    return render(request, "blog/index.html", {"categorie":categorie})

def vypis_autorov(request):
    autori = User.objects.all().order_by("meno")
    return render(request, "blog/index.html", {"autori":autori})