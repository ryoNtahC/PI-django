import random
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from skola.models import *

f = open("ULICE69.csv", "r", encoding="utf8")
lines = f.readlines()

studenti = Student.objects.all()

for i in range(5):
    random_line = random.choice(lines)
    print(f'random riadok {random_line}')

for i in studenti:
    print(i.pk)
    random_line = random.choice(lines)
    ulica, psc, obec = random_line.split(";")
    i.ulica = f'{ulica} {random.randint(1,2000)}'
    i.psc = f'{psc}'
    i.obec = f'{obec}'
    i.save()