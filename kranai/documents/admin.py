from django.contrib import admin
from .models import Document, Vehicle


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document_number', 'cargo_name', 'quantity', 'created_by', 'created_at')
    search_fields = ('document_number', 'cargo_name')
    list_filter = ('created_at', "created_by")


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'model')  # Rodomi laukai
    search_fields = ('registration_number', 'model')  # Paieška
    ordering = ('registration_number',)  # Rikiavimas pagal numerį
