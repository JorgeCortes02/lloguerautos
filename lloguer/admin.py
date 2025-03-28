from django.contrib import admin

from .models import *

class AutomobilAdmin(admin.ModelAdmin):
    list_display = ('marca', 'model', 'matricula')  
    

admin.site.register(Automobil, AutomobilAdmin)


class ReservaAdmin(admin.ModelAdmin):
    list_display = ('automobil', 'usuario', 'data_inici', 'data_fi') 
    
admin.site.register(Reserva, ReservaAdmin)