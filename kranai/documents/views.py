from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import Document
from .forms import FreightBillForm, PlatformTransferForm


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
            document.document_type = 'freight'
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
            document.document_type = 'platform'
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
    if document.document_type == 'freight':
        template_path = 'documents/freight_bill_template.html'
    elif document.document_type == 'platform':
        template_path = 'documents/platform_transfer_template.html'
    else:
        return HttpResponse('Neteisingas dokumento tipas')

    # Ruošiame HTML turinį
    context = {'document': document}
    html_string = render_to_string(template_path, context)

    # Generuojame PDF su WeasyPrint
    pdf_file = HTML(string=html_string).write_pdf()

    # Gražiname PDF kaip atsisiuntimą
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="document_{document.pk}.pdf"'
    return response


# Dokumento redagavimas
@login_required
def document_update(request, pk):
    document = get_object_or_404(Document, pk=pk, created_by=request.user)
    if document.document_type == 'freight':
        form_class = FreightBillForm
    elif document.document_type == 'platform':
        form_class = PlatformTransferForm
    else:
        return HttpResponse('Neteisingas dokumento tipas')

    if request.method == 'POST':
        form = form_class(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = form_class(instance=document)
    return render(request, 'documents/document_form.html', {'form': form, 'title': 'Redaguoti Dokumentą'})


# Dokumento šalinimas
@staff_member_required
def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    document.delete()
    return redirect('document_list')
