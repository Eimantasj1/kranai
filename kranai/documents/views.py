from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import Document
from .forms import FreightBillForm, PlatformTransferForm

# Dokumento tipo pasirinkimas
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
            document.driver_name = f"{request.user.first_name} {request.user.last_name}"
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
            document.delivered_by = f"{request.user.first_name} {request.user.last_name}"  # Automatinis priskyrimas
            document.save()
            return redirect('document_list')
    else:
        form = PlatformTransferForm()
    
    return render(request, 'documents/document_form.html', {'form': form, 'title': 'Platformos Priėmimo-Perdavimo Aktas'})


# Dokumentų sąrašas
@login_required
def document_list(request):
    documents = Document.objects.all() if request.user.is_staff else Document.objects.filter(created_by=request.user)
    return render(request, 'documents/document_list.html', {'documents': documents})


# PDF generavimas (atskirai peržiūrai ir atsisiuntimui)
@login_required
def render_pdf_view(request, pk, preview=False):
    document = get_object_or_404(Document, pk=pk)
    
    if document.document_type == 'freight':
        template_path = 'documents/freight_bill_template.html'
    elif document.document_type == 'platform':
        template_path = 'documents/platform_transfer_template.html'
    else:
        return HttpResponse('Neteisingas dokumento tipas', status=400)

    # Sukuriame HTML turinį
    context = {'document': document}
    html_string = render_to_string(template_path, context)
    pdf_file = HTML(string=html_string).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')

    # Peržiūrai atidaro naršyklėje, atsisiuntimui – prideda `attachment`
    if preview:
        response['Content-Disposition'] = f'inline; filename="document_{document.pk}.pdf"'
    else:
        response['Content-Disposition'] = f'attachment; filename="document_{document.pk}.pdf"'

    return response


# Dokumento redagavimas
@login_required
def document_update(request, pk):
    document = get_object_or_404(Document, pk=pk, created_by=request.user)
    
    form_class = FreightBillForm if document.document_type == 'freight' else PlatformTransferForm
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
