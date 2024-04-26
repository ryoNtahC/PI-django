import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from skola.models import *
import random, datetime

#Trieda.objects.all().delete()
#Student.objects.all().delete()
#Ucitel.objects.all().delete()



dnesny_rok = datetime.date.today().year

triedy = []
for rocnik in range(1,5):
    if rocnik == 1:
        vek = 16
    elif rocnik == 2:
        vek = 17
    elif rocnik == 3:
        vek = 18
    elif rocnik == 4:
        vek = 19
    for pismeno in ['A', 'B', 'C', 'D']:
        triedy.append(f'{rocnik}.{pismeno}')
        #Trieda.objects.create(nazov=f'{rocnik}.{pismeno}')

"""""
triedy = []
for rocnik in range(1,5):
    for pismeno in ['A','B','C','D']:
       triedy.append(f'{rocnik}.{pismeno}')
       Trieda.objects.create(nazov=f'{rocnik}.{pismeno}')
"""""
"""""
fmena = open('mena.txt', 'r', encoding='utf-8')
mena = fmena.read().splitlines()

fpriezviska = open('priezviska.txt', 'r', encoding='utf-8')
priezviska = fpriezviska.read().splitlines()

for i in range(20):
    meno = random.choice(mena)
    priezvisko = random.choice(priezviska)
    titul = random.choice(["Mgr.", "Ing.", "PhDr.", "PaeDr.", ""])
    if i < len(triedy):
        trieda = Trieda.objects.get(nazov=triedy[i])
        Ucitel.objects.create(titul=titul, meno=meno, priezvisko=priezvisko, trieda=trieda)
    else:
        Ucitel.objects.create(meno=meno, priezvisko=priezvisko)


for i in range(100):
    meno = random.choice(mena)
    priezvisko = random.choice(priezviska)
    trieda = Trieda.objects.get(nazov=random.choice(triedy))
    Student.objects.create(meno=meno, priezvisko=priezvisko, trieda=trieda)

"""""

studenti = Student.objects.all()
ucitelia = Ucitel.objects.all()

def ziskaj_datum(vek):
    mesiac = random.randint(1,12)
    rok_narodenia  = dnesny_rok - vek
    if mesiac == "1" or "3" or "5" or "7" or "8" or "10" or "12":
        den = random.randint(1,31)
    elif mesiac == "2":
        if rok_narodenia/4 == 0:
            den = random.randint(1,29) 
        else:
            den = random.randint(1,28)
    else:
        den = random.randint(1,30)
    return f"{den}. {mesiac}. {rok_narodenia}"
    


for j in studenti:
    vek_student = j.vek
    j.rok_narodenia = dnesny_rok - vek_student
    j.datum_narodenia = ziskaj_datum(vek_student)
    j.save()

for k in ucitelia:
    vek_ucitel = random.randint(25,61)
    k.rok_narodenia = dnesny_rok - vek_ucitel
    k.datum_narodenia = ziskaj_datum(vek_ucitel)
    k.save()