from django.db import models
from django.contrib.auth.models import User




class Document(models.Model):
    document_number = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    #dokumento laukai
    cargo_name = models.CharField("Krovinio pavadinimas", max_length=225)
    quantity = models.FloatField("Kiekis litrais arba kg")
    vehicle_make = models.CharField("Automobilio markė", max_length=100)
    vehicle_plate = models.CharField("Valstybinis numeris", max_length=20)
    load_location =models.CharField("Pakrovimo vieta", max_length=255)
    unload_location = models.CharField("Vairuotojo vardas, pavardė", max_length=255)

    def __str__(self):
        return f"Dokumentas {self.document_number}"