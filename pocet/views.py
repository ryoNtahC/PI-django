from django.shortcuts import render
import random
from . models import *
from calc.models import *


def pocet(request):
    stena = Priklad.objects.count()
    cislo = random.randint(1,stena)
    priklad = Priklad.objects.get(id = cislo)  
    skore = 0
    bad = 0
    bodiky = High_score.objects.get(id = 1)

    if request.method == "GET":
        return render(request, "pocet/index.html", {"priklad": priklad, "skore":skore, "bad":bad, "bodiky":bodiky})

    else:
        try: 
            vysledok = float(request.POST["vysledok"])
        except:
            vysledok = "Zadaj čísla!"
            skore = int(request.POST["skore"]) 
            return render(request, "pocet/index.html", {"vysledok":vysledok, "priklad": priklad, "skore":skore, "bad":bad, "bodiky":bodiky})

        skore = int(request.POST["skore"]) 

        if float(request.POST["vysledok"]) == float(request.POST["spravny_vysledok"]):
            vysledok = "Správne, si frajer!!!"
            skore += 1
            if skore > bodiky.score:
                bodiky.score = skore
                bodiky.save()
            return render(request, "pocet/index.html", {"vysledok":vysledok, "priklad": priklad, "skore":skore, "bad":bad, "bodiky":bodiky})

        else:
            vysledok = "Zadal si zlý výsledok, skús ďalší príklad!"
            bad += 1

        return render(request, "pocet/index.html", {"vysledok":vysledok, "priklad": priklad, "skore":skore, "bad":bad, "bodiky":bodiky})