from django.db import models
from django.utils import timezone

class Categories(models.Model):
    nazov = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nazov}"

class Products(models.Model):
    nazov = models.CharField(max_length=20)
    popis = models.TextField()
    cena = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nazov} {self.popis} {self.cena} {self.category}"


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length = 80)
    heslo = models.CharField(max_length = 25)

    def __str__(self):
        return f"{self.username} {self.email} {self.heslo}"
    
class Order(models.Model):
    zakaznik = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    produkt = models.ForeignKey(Products,on_delete=models.SET_NULL, null=True, blank=True)
    datum = models.DateTimeField(default = timezone.now)
