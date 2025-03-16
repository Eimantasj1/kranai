from django import forms
from .models import Document, Vehicle

class FreightBillForm(forms.ModelForm):
    registration_number = forms.ModelChoiceField(
        queryset=Vehicle.objects.all(),
        empty_label="Pasirinkite valstybinį numerį",
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Valst. Nr."
    )

    class Meta:
        model = Document
        fields = [
            'document_number', 'cargo_name', 'quantity', 
            'receiver_name', 'phone', 
            'email', 'project_address', 'distance', 'delivery_info', 
            'registration_number',
            'loading_location', 'unloading_location'
        ]
        labels = {
            'document_number': 'Dokumento numeris',
            'cargo_name': 'Krovinio pavadinimas',
            'quantity': 'Kiekis',
            'receiver_name': 'Gavėjo vardas',
            'phone': 'Telefonas',
            'email': 'El. Paštas',
            'project_address': 'Adresas',
            'distance': 'Pravažiuota kilometrų',
            'delivery_info': 'Pristatymas / išvežimas',
            'registration_number': 'Valst. Nr.',
            'loading_location': 'Pakrovimo vieta',
            'unloading_location': 'Iškrovimo vieta',
        }

class PlatformTransferForm(forms.ModelForm):
    registration_number = forms.ModelChoiceField(
        queryset=Vehicle.objects.all(),
        empty_label="Pasirinkite valstybinį numerį",
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'vehicle-select'}),
        label="Valstybinis numeris"
    )

    model = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control', 'id': 'vehicle-model'}),
        required=False
    )

    class Meta:
        model = Document
        fields = [
            'document_number', 'model', 'registration_number', 
            'client_name', 'lifting_capacity', 'days_worked', 'daily_price',
            'start_date', 'end_date', 'km_price', 'client_code', 
            'received_by', 'distance', 'delivery_info',
            'phone', 'email', 'project_address', 'transport_price_delivery', 'transport_price_pickup'
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
            'received_by': 'Įrangą priėmęs asmuo',
            'distance': 'Pravažiuota kilometrų',
            'delivery_info': 'Pristatymas / išvežimas',
            'phone': 'Telefonas',
            'email': 'El. Paštas',
            'project_address': 'Adresas',
            'transport_price_delivery': 'Pristatymo mokestis (€)',
            'transport_price_pickup': 'Išvežimo mokestis (€)',
        }

    def __init__(self, *args, **kwargs):
        """ Automatiškai užpildo 'delivered_by' pagal vartotojo vardą """
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['delivered_by'] = forms.CharField(
                initial=user.get_full_name(),
                widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
                required=False
            )
