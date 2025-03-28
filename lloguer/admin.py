from django.contrib import admin

from .models import *

class AutomobilAdmin(admin.ModelAdmin):
    list_display = ('marca', 'model', 'matricula')  # Muestra estos campos en la lista
    

admin.site.register(Automobil, AutomobilAdmin)