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


# Forma Mobilios platformos aktui
class PlatformTransferForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'document_number', 'model', 'registration_number',
            'client_name', 'lifting_capacity', 'days_worked', 'daily_price'
        ]


# Bendroji forma dokumentų kūrimui (jeigu reikia)
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
