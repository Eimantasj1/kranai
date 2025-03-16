from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    registration_number = models.CharField("Valstybinis numeris", max_length=20, unique=True)
    model = models.CharField("Transporto priemonės modelis", max_length=50)

    def __str__(self):
        return self.registration_number

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
        default='freight'
    )
    document_number = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="documents")
    created_at = models.DateTimeField(auto_now_add=True)

    carrier_name = models.CharField(
        "Vežėjo pavadinimas ir adresas",
        max_length=255,
        default="UAB ,,KĖDAINIŲ KRANAI‘‘ Įmonės kodas 302742708 Parko g. 20, Juodkaimių k. Kėdainių r.",
        editable=False
    )
    driver_name = models.CharField("Vairuotojo vardas", max_length=255, blank=True, null=True)
    loading_location = models.CharField("Pakrovimo vieta", max_length=255, blank=True, null=True)
    unloading_location = models.CharField("Iškrovimo vieta", max_length=255, blank=True, null=True)

    # Krovinio važtaraščio laukai
    cargo_name = models.CharField("Krovinio pavadinimas", max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField("Kiekis", blank=True, null=True)
    sender_name = models.CharField("Siuntėjo vardas", max_length=255, blank=True, null=True)
    receiver_name = models.CharField("Gavėjo vardas", max_length=255, blank=True, null=True)
    phone = models.CharField("Telefonas", max_length=20, blank=True, null=True)
    project_address = models.CharField("Adresas", max_length=255, blank=True, null=True)
    email = models.EmailField("El. Paštas", blank=True, null=True)

    # Platformos akto laukai
    model = models.CharField("Markė/Modelis", max_length=255, blank=True, null=True)
    registration_number = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Valstybinis numeris")
    client_name = models.CharField("Užsakovas", max_length=255, blank=True, null=True)
    lifting_capacity = models.CharField("Keliamoji galia, strėlės siekis", max_length=100, blank=True, null=True)
    days_worked = models.PositiveIntegerField("Dirbtos paros", blank=True, null=True)
    daily_price = models.DecimalField("Paros kaina", max_digits=10, decimal_places=2, blank=True, null=True)
    start_date = models.DateField("Nuomos pradžios data", blank=True, null=True)
    end_date = models.DateField("Nuomos pabaigos data", blank=True, null=True)
    km_price = models.DecimalField("Kilometro kaina", max_digits=10, decimal_places=2, blank=True, null=True)
    client_code = models.CharField("Užsakovo kodas", max_length=100, blank=True, null=True)
    delivered_by = models.CharField("Įrangą pristatęs asmuo", max_length=255, blank=True, null=True)
    received_by = models.CharField("Įrangą priėmęs asmuo", max_length=255, blank=True, null=True)

    # Nauji laukai
    distance = models.CharField("Pravažiuota kilometrų", max_length=100, blank=True, null=True)
    delivery_info = models.CharField("Pristatymas / išvežimas", max_length=255, blank=True, null=True)

    transport_price_delivery = models.DecimalField(
        "Pristatymo mokestis (€)", max_digits=10, decimal_places=2, blank=True, null=True
    )
    transport_price_pickup = models.DecimalField(
        "Išvežimo mokestis (€)", max_digits=10, decimal_places=2, blank=True, null=True
    )

    def save(self, *args, **kwargs):
        if not self.driver_name:
            self.driver_name = f"{self.created_by.first_name} {self.created_by.last_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_document_type_display()} - {self.document_number}"
