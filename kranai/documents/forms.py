from django import forms
from .models import Document


class FreightBillForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'document_number', 'document_type', 'cargo_name', 'quantity',
            'sender_name', 'receiver_name', 'phone', 'project_address'
        ]
        labels = {
            'document_number': 'Dokumento numeris',
            'document_type': 'Dokumento tipas',
            'cargo_name': 'Krovinio pavadinimas',
            'quantity': 'Kiekis',
            'sender_name': 'Siuntėjo vardas',
            'receiver_name': 'Gavėjo vardas',
            'phone': 'Telefonas',
            'project_address': 'Projekto adresas',
        }

class PlatformTransferForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'document_number', 'document_type', 'model', 'registration_number',
            'client_name', 'lifting_capacity', 'days_worked', 'daily_price',
            'start_date', 'end_date', 'km_price', 'client_code',
            'delivered_by', 'received_by',
        ]
        labels = {
            'document_number': 'Dokumento numeris',
            'document_type': 'Dokumento tipas',
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
        }
