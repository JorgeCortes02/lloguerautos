from django.contrib import admin

from .models import *

class AutomobilAdmin(admin.ModelAdmin):
    list_display = ('marca', 'model', 'matricula')  # Muestra estos campos en la lista
    

admin.site.register(Automobil, AutomobilAdmin)


class ReservaAdmin(admin.ModelAdmin):
    list_display = ('automobil', 'usuario', 'data_inici', 'data_fi')  # Muestra estos campos
    search_fields = ('automobil__marca', 'usuario__username')  # Permite búsqueda
    list_filter = ('data_inici', 'automobil')  # Filtros útiles
    ordering = ('-data_inici',)  # Orden por fecha descendente

admin.site.register(Reserva, ReservaAdmin)