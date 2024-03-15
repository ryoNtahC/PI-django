from django.shortcuts import render, HttpResponse
from . models import *

def vypis_skola(request):
    triedy = Trieda.objects.all().order_by("nazov")
    studenti = Student.objects.all().order_by("priezvisko")
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {"triedy":triedy, "ucitelia":ucitelia, "studenti":studenti})

def vypis_studenta(request):
    studenti = Student.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {"studenti":studenti})

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
    return render(request, 'skola/student_detail.html', {'student':student, 'triedos':triedos, 'ucitelos':ucitelos})
    

def vypis_ucitel(request, ucitel):
    ucitel = Ucitel.objects.get(id = ucitel)
    triedos = Trieda.objects.get(nazov = ucitel.trieda)
    return render(request, 'skola/ucitel_detail.html', {'ucitel':ucitel, 'triedos':triedos})





