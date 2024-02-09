from django.shortcuts import render, HttpResponse
from . models import *

def calc(request):
    if request.method == "GET":
        return render(request, "calc/index.html")
    else:
        try:
            a = float(request.POST["a"])
            b = float(request.POST["b"])
        except:
            vysledok = "zadaj číslo!"
            return render(request, 'calc/index.html', {"vysledok":vysledok})
        operator = request.POST["operator"]
        if operator == "+":
            vysledok = a + b
        elif operator == "-":
            vysledok = a - b
        elif operator == "*":
             vysledok = a * b
        elif operator == "/":
              if b == 0:
                vysledok = "Nulou mi tu deliť nebudeš!"
                return render(request, 'calc/index.html', {"vysledok":vysledok})
              else:
                vysledok = a / b
        try:
            priklad_check = Priklad.objects.get(a=a, b=b, operator=operator)
        except:
            priklad = Priklad(
                a = a,
                b = b,
                operator = operator,
                vysledok = vysledok,
            )
            priklad.save()
        return render(request, 'calc/index.html', {"vysledok":vysledok, "a":a, "b":b, "operator":operator})
