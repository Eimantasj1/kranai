from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'document_number', 'cargo_name', 'quantity',
            'model', 'registration_number', 'sender_name', 'receiver_name',
            'lifting_capacity', 'phone', 'daily_price', 'email',
            'client_name', 'km_price', 'project_address', 'distance', 'days_worked'
        ]
