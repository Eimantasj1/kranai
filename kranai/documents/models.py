from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    document_number = models.CharField(max_length=100)
    cargo_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="documents"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # Papildomi laukeliai
    model = models.CharField(max_length=255, blank=True, null=True)
    registration_number = models.CharField(max_length=100, blank=True, null=True)
    sender_name = models.CharField(max_length=255, blank=True, null=True)
    receiver_name = models.CharField(max_length=255, blank=True, null=True)
    lifting_capacity = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    daily_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    client_name = models.CharField(max_length=255, blank=True, null=True)
    km_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    project_address = models.CharField(max_length=255, blank=True, null=True)
    distance = models.PositiveIntegerField(blank=True, null=True)
    days_worked = models.PositiveIntegerField(blank=True, null=True)