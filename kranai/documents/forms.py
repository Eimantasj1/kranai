from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'document_number', 'cargo_name', 'quantity',
            'vehicle_make', 'vehicle_plate', 'load_location',
            'unload_location', 'driver_name'
        ]