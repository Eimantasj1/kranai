from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    # Dokumento tipų pasirinkimai
    DOCUMENT_TYPE_CHOICES = [
        ('freight', 'Krovinio važtaraštis'),
        ('platform', 'Mobilios alkūninės darbo platformos aktas'),
    ]

    # Bendri laukai visiems dokumentams
    document_type = models.CharField(
        max_length=50,
        choices=DOCUMENT_TYPE_CHOICES,
        default='freight'  # Numatytasis tipas
    )
    document_number = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="documents"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # Krovinio važtaraščio laukai
    cargo_name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    sender_name = models.CharField(max_length=255, blank=True, null=True)
    receiver_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    project_address = models.CharField(max_length=255, blank=True, null=True)

    # Platformos akto laukai
    model = models.CharField(max_length=255, blank=True, null=True)
    registration_number = models.CharField(max_length=100, blank=True, null=True)
    client_name = models.CharField(max_length=255, blank=True, null=True)
    lifting_capacity = models.CharField(max_length=100, blank=True, null=True)
    days_worked = models.PositiveIntegerField(blank=True, null=True)
    daily_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.get_document_type_display()} - {self.document_number}"
