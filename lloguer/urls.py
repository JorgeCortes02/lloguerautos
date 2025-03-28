from . import views
from django.urls import path
urlpatterns = [
    path('autos/', views.mostrar_autos, name='mostrar_autos'),  # Ruta a la vista
]