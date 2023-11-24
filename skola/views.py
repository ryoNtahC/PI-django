from django.shortcuts import render, HttpResponse
from . models import *

def vypis_students(request):
    studenti = Student.objects.all()
    return(HttpResponse(studenti))
