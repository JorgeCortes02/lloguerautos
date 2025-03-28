from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10, unique=True)  # Unique evita duplicados

    def __str__(self):
        return f"{self.marca} {self.model} ({self.matricula})"
    
class Reserva(models.Model):
    automobil = models.ForeignKey(Automobil, on_delete=models.CASCADE)  # Relación con Automobil
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con User
    data_inici = models.DateField()  # Fecha de inicio del alquiler
    data_fi = models.DateField()  # Fecha de fin del alquiler

    class Meta:
        unique_together = ('automobil', 'data_inici')  # Clave única para evitar dobles reservas

    def __str__(self):
        return f"Reserva de {self.automobil} por {self.usuario.username} el {self.data_inici}"

