from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from random import randint, choice
from datetime import timedelta

from lloguer.models import Automobil, Reserva  

faker = Faker(["es_CA", "es_ES"])

class Command(BaseCommand):
    help = "Genera datos falsos de Automobil, User y Reserva"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Generando datos falsos..."))

        # Crear 4 Automóviles
        automoviles = []
        for _ in range(4):
            auto = Automobil.objects.create(
                marca=faker.company(),
                model=faker.word(),
                matricula=faker.unique.license_plate()
            )
            automoviles.append(auto)

        # Crear 8 Usuarios con nombres aleatorios
        usuarios = []
        for _ in range(8):
            username = faker.unique.user_name()  # Genera un nombre de usuario aleatorio
            email = faker.unique.email()  # Email único aleatorio
            user = User.objects.create_user(username=username, email=email, password="12345")
            usuarios.append(user)

        # Crear Reservas (1-2 por usuario)
        for usuario in usuarios:
            num_reservas = randint(1, 2)
            for _ in range(num_reservas):
                coche = choice(automoviles)  # Selecciona un coche aleatorio
                data_inici = faker.date_between(start_date="-30d", end_date="+30d")  # Último/Próximo mes
                data_fi = data_inici + timedelta(days=randint(1, 5))  # Entre 1 y 5 días de alquiler
                
                # Evita reservas duplicadas en la misma fecha
                if not Reserva.objects.filter(automobil=coche, data_inici=data_inici).exists():
                    Reserva.objects.create(
                        automobil=coche,
                        usuario=usuario,
                        data_inici=data_inici,
                        data_fi=data_fi
                    )

        self.stdout.write(self.style.SUCCESS("Datos falsos creados con éxito. 🚗🎉"))