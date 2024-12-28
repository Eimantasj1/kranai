from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from django.conf import settings
from .models import Document
from .forms import DocumentForm, FreightBillForm, PlatformTransferForm


# Funkcija dokumento tipo pasirinkimui
@login_required
def document_select(request):
    return render(request, 'documents/document_select.html')


# Krovinio važtaraščio kūrimas
@login_required
def document_create_freight(request):
    if request.method == 'POST':
        form = FreightBillForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.created_by = request.user
            document.document_type = 'freight_bill'
            document.save()
            return redirect('document_list')
    else:
        form = FreightBillForm()
    return render(request, 'documents/document_form.html', {'form': form, 'title': 'Krovinio Važtaraštis'})


# Platformos perdavimo akto kūrimas
@login_required
def document_create_platform(request):
    if request.method == 'POST':
        form = PlatformTransferForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.created_by = request.user
            document.document_type = 'platform_transfer'
            document.save()
            return redirect('document_list')
    else:
        form = PlatformTransferForm()
    return render(request, 'documents/document_form.html', {'form': form, 'title': 'Platformos Priėmimo-Perdavimo Aktas'})


# Dokumentų sąrašas
@login_required
def document_list(request):
    if request.user.is_staff:
        documents = Document.objects.all()
    else:
        documents = Document.objects.filter(created_by=request.user)
    return render(request, 'documents/document_list.html', {'documents': documents})


# PDF generavimas
@login_required
def render_pdf_view(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if document.document_type == 'freight_bill':
        template_path = 'documents/freight_bill_template.html'
    else:
        template_path = 'documents/platform_transfer_template.html'

    context = {'document': document}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="document_{document.pk}.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    # Tvarkome CSS kelius
    def link_callback(uri, rel):
        s_path = os.path.join(settings.STATICFILES_DIRS[0], uri.replace(settings.STATIC_URL, ""))
        if not os.path.isfile(s_path):
            raise Exception(f"Static file not found: {s_path}")
        return s_path

    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    if pisa_status.err:
        return HttpResponse('PDF generavimo klaida')
    return response


# Dokumento redagavimas
@login_required
def document_update(request, pk):
    document = get_object_or_404(Document, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(instance=document)
    return render(request, 'documents/document_form.html', {'form': form})


# Dokumento šalinimas
@staff_member_required
def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    document.delete()
    return redirect('document_list')
