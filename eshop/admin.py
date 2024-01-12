from django.contrib import admin
from . models import Categories, Products, User, Order

admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(User)
admin.site.register(Order)
