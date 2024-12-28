from django import forms
from .models import Document


# Forma Krovinio važtaraščiui
class FreightBillForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'document_number', 'cargo_name', 'quantity',
            'sender_name', 'receiver_name', 'phone', 'project_address'
        ]
        labels = {
            'document_number': 'Dokumento numeris',
            'cargo_name': 'Krovinio pavadinimas',
            'quantity': 'Kiekis',
            'sender_name': 'Siuntėjo vardas',
            'receiver_name': 'Gavėjo vardas',
            'phone': 'Telefonas',
            'project_address': 'Projekto adresas',
        }
        help_texts = {
            'document_number': 'Įveskite dokumento numerį.',
            'cargo_name': 'Nurodykite krovinio pavadinimą.',
            'quantity': 'Nurodykite krovinio kiekį.',
            'sender_name': 'Įveskite siuntėjo vardą arba įmonės pavadinimą.',
            'receiver_name': 'Įveskite gavėjo vardą arba įmonės pavadinimą.',
            'phone': 'Įrašykite telefono numerį.',
            'project_address': 'Nurodykite projekto adresą.',
        }


# Forma Mobilios platformos aktui
class PlatformTransferForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'document_number', 'model', 'registration_number',
            'client_name', 'lifting_capacity', 'days_worked', 'daily_price',
            'start_date', 'end_date', 'km_price', 'client_code', 
            'delivered_by', 'received_by',
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
        }
        help_texts = {
            'document_number': 'Įveskite dokumento numerį.',
            'model': 'Nurodykite platformos markę ir modelį.',
            'registration_number': 'Įrašykite valstybinį numerį.',
            'client_name': 'Nurodykite užsakovą arba įmonę.',
            'lifting_capacity': 'Įrašykite keliamąją galią ir strėlės siekį.',
            'days_worked': 'Įveskite dirbtų parų skaičių.',
            'daily_price': 'Nurodykite nuomos kainą per parą.',
            'start_date': 'Įrašykite nuomos pradžios datą.',
            'end_date': 'Įrašykite nuomos pabaigos datą.',
            'km_price': 'Nurodykite kilometro kainą.',
            'client_code': 'Įrašykite užsakovo kodą.',
            'delivered_by': 'Įrašykite pristatymo asmens vardą ir pavardę.',
            'received_by': 'Įrašykite priėmusio asmens vardą ir pavardę.',
        }
