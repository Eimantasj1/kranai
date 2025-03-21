# Generated by Django 5.1.3 on 2025-02-20 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0008_document_transport_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='transport_price',
        ),
        migrations.AddField(
            model_name='document',
            name='transport_price_delivery',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Pristatymo mokestis (€)'),
        ),
        migrations.AddField(
            model_name='document',
            name='transport_price_pickup',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Išvežimo mokestis (€)'),
        ),
    ]
