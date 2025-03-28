from django.shortcuts import render
from .models import Automobil


def mostrar_autos(request):
   
    automoviles = Automobil.objects.all()

   
    return render(request, 'lloguer/autos.html', {'automoviles': automoviles})
