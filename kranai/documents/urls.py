from django.urls import path
from . import views

urlpatterns = [
    path('', views.document_list, name='document_list'),
    path('select/', views.document_select, name='document_select'),  # Dokumento tipo pasirinkimas
    path('new/freight/', views.document_create_freight, name='document_create_freight'),  # Krovinio važtaraštis
    path('new/platform/', views.document_create_platform, name='document_create_platform'),  # Platformos aktas
    path('<int:pk>/edit/', views.document_update, name='document_update'),
    path('<int:pk>/delete/', views.document_delete, name='document_delete'),
    path('<int:pk>/pdf/', views.render_pdf_view, name='document_pdf'),
]
