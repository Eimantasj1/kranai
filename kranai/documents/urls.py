from django.urls import path
from . import views

urlpatterns = [
    path('', views.document_list, name='document_list'),  # Dokumentų sąrašas
    path('select/', views.document_select, name='document_select'),  # Dokumento tipo pasirinkimas
    path('new/freight/', views.document_create_freight, name='document_create_freight'),  # Naujo Krovinio važtaraščio kūrimas
    path('new/platform/', views.document_create_platform, name='document_create_platform'),  # Naujo Platformos akto kūrimas
    path('<int:pk>/edit/', views.document_update, name='document_update'),  # Dokumento redagavimas
    path('<int:pk>/delete/', views.document_delete, name='document_delete'),  # Dokumento ištrynimas
    path('<int:pk>/pdf/', views.render_pdf_view, name='document_pdf'),  # Dokumento PDF atsisiuntimas
    path('<int:pk>/view/', views.render_pdf_view, {'preview': True}, name='document_view'),  # Dokumento peržiūra
]
