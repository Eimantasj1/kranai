from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.document_list, name='document_list'),
    path('new/', views.document_create, name='document_create'),
    path('<int:pk>/edit/', views.document_update, name='document_update'),
    path('<int:pk>/delete/', views.document_delete, name='document_delete'),
    path('<int:pk>/pdf/', views.render_pdf_view, name='document_pdf'),
]