from django import forms
from .models import Document

class FreightBillForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'document_number', 'cargo_name', 'quantity', 
            'sender_name', 'receiver_name', 'phone', 
            'email', 'project_address', 'distance', 'delivery_info', 
            'driver_name', 'carrier_name', 'registration_number',
            'loading_location', 'unloading_location'
        ]
        labels = {
            'document_number': 'Dokumento numeris',
            'cargo_name': 'Krovinio pavadinimas',
            'quantity': 'Kiekis',
            'sender_name': 'Siuntėjo vardas',
            'receiver_name': 'Gavėjo vardas',
            'phone': 'Telefonas',
            'email': 'El. Paštas',
            'project_address': 'Adresas',
            'distance': 'Pravažiuota kilometrų',
            'delivery_info': 'Pristatymas / išvežimas',
            'driver_name': 'Vairuotojas',
            'carrier_name': 'Vežėjas',
            'registration_number': 'Valst. Nr.',
            'loading_location': 'Pakrovimo vieta',
            'unloading_location': 'Iškrovimo vieta',
        }

class PlatformTransferForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'document_number', 'model', 'registration_number', 
            'client_name', 'lifting_capacity', 'days_worked', 'daily_price',
            'start_date', 'end_date', 'km_price', 'client_code', 
            'delivered_by', 'received_by', 'distance', 'delivery_info',
            'phone', 'email', 'project_address'
        ]
        labels = {
            'document_number': 'Dokumento numeris',
            'model': 'Markė/Modelis',
            'registration_number': 'Valstybinis numeris',
            'client_name': 'Užsakovas',
            'lifting_capacity': 'Keliamoji galia, strėlės siekis',
            'days_worked': 'Dirbtos paros',
            'daily_price': 'Paros kaina',
            'start_date': 'Nuomos pradžios data',
            'end_date': 'Nuomos pabaigos data',
            'km_price': 'Kilometro kaina',
            'client_code': 'Užsakovo kodas',
            'delivered_by': 'Nuomotojo įrangą pristatęs asmuo',
            'received_by': 'Nuomininko priėmęs asmuo',
            'distance': 'Pravažiuota kilometrų',
            'delivery_info': 'Pristatymas / išvežimas',
            'phone': 'Telefonas',
            'email': 'El. Paštas',
            'project_address': 'Adresas',
        }
