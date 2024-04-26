from django.shortcuts import render, HttpResponse
from . models import *
from . forms import *

def vypis_skola(request):
    triedy = Trieda.objects.all().order_by("nazov")
    studenti = Student.objects.all().order_by("priezvisko")
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    kruzky = Kruzok.objects.all().order_by("nazov")
    return render(request, "skola/index.html", {"triedy":triedy, "ucitelia":ucitelia, "studenti":studenti, "kruzky":kruzky})

def vypis_studenta(request):
    studenti = Student.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {"studenti":studenti})


def vypis_kruzku(request):
    kruzky = Kruzok.objects.all().order_by("id")
    return render(request, "skola/index.html", {"kruzky":kruzky})

def vypis_triedy(request):
    triedy = Trieda.objects.all().order_by("nazov")
    return render(request, "skola/index.html", {"triedy":triedy})

def vypis_ucitela(request):
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {"ucitelia":ucitelia})

def vypis_trieda(request, trieda):
    trieda_obj = Trieda.objects.get(nazov=trieda)
    studenti = Student.objects.filter(trieda_id=trieda_obj.pk).order_by("priezvisko")
    studenti_list = []
    for student in studenti:
        studenti_list.append(f"{student.meno} {student.priezvisko}")
    ucitel = Ucitel.objects.get(trieda_id=trieda_obj.pk)
    ucitel = f"{ucitel.titul} {ucitel.meno} {ucitel.priezvisko}"
    #return HttpResponse(f'{trieda}<br>{ucitel}<br>{studenti_list}')
    return render(request, "skola/trieda_list.html", {"trieda":trieda, "ucitel":ucitel, "studenti":studenti_list})


def vypis_student(request, student):
    student = Student.objects.get(id = student)
    triedos = Trieda.objects.get(nazov = student.trieda)
    ucitelos = Ucitel.objects.get(trieda = triedos.id)
    kruzky = Kruzok.objects.filter(student = student)
    return render(request, 'skola/student_detail.html', {'student':student, 'triedos':triedos, 'ucitelos':ucitelos, 'kruzky':kruzky})
    

def vypis_ucitel(request, ucitel):
    ucitel = Ucitel.objects.get(id = ucitel)
    triedos = Trieda.objects.get(nazov = ucitel.trieda)
    try:
        kruzok = Kruzok.objects.get(ucitel = ucitel.pk)
    except:
        kruzok = ""
    return render(request, 'skola/ucitel_detail.html', {'ucitel':ucitel, 'triedos':triedos, 'kruzok':kruzok})

def vypis_kruzok(request, kruzok):
    kruzok = Kruzok.objects.get(nazov = kruzok)
    ucitel = Ucitel.objects.get(kruzok = kruzok)
    student = Student.objects.filter(kruzok = kruzok)
    return render(request, 'skola/kruzok_detail.html', {'ucitel':ucitel, 'kruzok':kruzok, 'student':student})


def pridaj_uzivatel(request):
    if request.method == "POST":
        uzivatel = Uzivatel(
            meno = request.POST["Meno"],
            priezvisko = request.POST["Priezvisko"],
            email = request.POST["Email"],
            datum = request.POST["Datum"],
        )
        uzivatel.save()
        return HttpResponse("OK")
    else:
        return render(request, "skola/pridaj_uzivatel.html")
    
def pridaj_uzivatel2(request):
    if request.method == "POST":
        form = UzivatelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
    else:
        form = UzivatelForm()
        