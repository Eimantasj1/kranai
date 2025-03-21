# Generated by Django 5.1.3 on 2024-11-30 16:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_number', models.CharField(max_length=100)),
                ('cargo_name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=100, null=True)),
                ('sender_name', models.CharField(blank=True, max_length=255, null=True)),
                ('receiver_name', models.CharField(blank=True, max_length=255, null=True)),
                ('lifting_capacity', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('daily_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('client_name', models.CharField(blank=True, max_length=255, null=True)),
                ('km_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('project_address', models.CharField(blank=True, max_length=255, null=True)),
                ('distance', models.PositiveIntegerField(blank=True, null=True)),
                ('days_worked', models.PositiveIntegerField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
