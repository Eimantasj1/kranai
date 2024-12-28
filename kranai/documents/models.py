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
    cargo_name = models.CharField("Krovinio pavadinimas", max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField("Kiekis", blank=True, null=True)
    sender_name = models.CharField("Siuntėjo vardas", max_length=255, blank=True, null=True)
    receiver_name = models.CharField("Gavėjo vardas", max_length=255, blank=True, null=True)
    phone = models.CharField("Telefonas", max_length=20, blank=True, null=True)
    project_address = models.CharField("Adresas", max_length=255, blank=True, null=True)

    # Platformos akto laukai
    model = models.CharField("Markė/Modelis", max_length=255, blank=True, null=True)
    registration_number = models.CharField("Valstybinis numeris", max_length=100, blank=True, null=True)
    client_name = models.CharField("Užsakovas", max_length=255, blank=True, null=True)
    lifting_capacity = models.CharField("Keliamoji galia, strėlės siekis", max_length=100, blank=True, null=True)
    days_worked = models.PositiveIntegerField("Dirbtos paros", blank=True, null=True)
    daily_price = models.DecimalField("Paros kaina", max_digits=10, decimal_places=2, blank=True, null=True)
    start_date = models.DateField("Nuomos pradžios data", blank=True, null=True)
    end_date = models.DateField("Nuomos pabaigos data", blank=True, null=True)
    km_price = models.DecimalField("Kilometro kaina", max_digits=10, decimal_places=2, blank=True, null=True)
    client_code = models.CharField("Užsakovo kodas", max_length=100, blank=True, null=True)
    delivered_by = models.CharField("Nuomotojo įrangą pristatęs asmuo", max_length=255, blank=True, null=True)
    received_by = models.CharField("Nuomininko priėmęs asmuo", max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.get_document_type_display()} - {self.document_number}"
