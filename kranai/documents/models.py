from django.db import models
from django.contrib.auth.models import User




class Document(models.Model):
    document_number = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    cargo_name = models.CharField(max_length=225)
    quantity = models.FloatField()
    vehicle_make = models.CharField(max_length=100)
    vehicle_plate = models.CharField(max_length=20)
    load_location =models.CharField(max_length=255)
    unload_location = models.CharField(max_length=255)

    def __str__(self):
        return f"Dokumentas {self.document_number}"