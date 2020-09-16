from django.contrib import admin

from django.contrib import admin
from .models import  Company,Teams,Gameweekwinner, Winner

admin.site.register(Company)
admin.site.register(Teams)
admin.site.register(Gameweekwinner)
admin.site.register(Winner)