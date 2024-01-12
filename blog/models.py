from django.db import models
from django.utils import timezone

class Categories(models.Model):
    nazov = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nazov}"
    
class User(models.Model):
    meno = models.CharField(max_length=25)
    priezvisko = models.CharField(max_length = 25)
    username = models.CharField(max_length = 25)

    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.username}"
    
class Post(models.Model):
    autor = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    nazov = models.CharField(max_length=30)
    datumvyt = models.DateTimeField(default = timezone.now)
    datumpub = models.DateTimeField(default = timezone.now)
    text = models.TextField()
    kategoria = models.ForeignKey(Categories,on_delete=models.SET_NULL, null=True, blank=True)


