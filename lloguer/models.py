from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10, unique=True)  # Unique evita duplicados

    def __str__(self):
        return f"{self.marca} {self.model} ({self.matricula})"

