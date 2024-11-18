from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from .models import Document
from .forms import DocumentForm


# PDF generavimas
@login_required
def render_pdf_view(request, pk):
    document = get_object_or_404(Document, pk=pk)
    template_path = 'documents/document_template.html'
    context = {'document': document}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="document.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    try:
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            raise Exception("PDF generavimo klaida.")
    except Exception as e:
        return HttpResponse(f'PDF generavimo klaida: {e}')
    return response


# Dokumentų sąrašas
@login_required
def document_list(request):
    if request.user.is_staff:
        documents = Document.objects.all()  # Administratoriai mato viską
    else:
        documents = Document.objects.filter(created_by=request.user)  # Vartotojas mato tik savo dokumentus
    print(f"Vartotojas prisijungęs: {request.user.is_authenticated}, Vartotojas: {request.user}")
    return render(request, 'documents/document_list.html', {'documents': documents})


# Naujo dokumento kūrimas
@login_required
def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.created_by = request.user
            document.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'documents/document_form.html', {'form': form})


# Dokumento redagavimas
@login_required
def document_update(request, pk):
    # Užtikriname, kad vartotojas gali redaguoti tik savo dokumentus
    document = get_object_or_404(Document, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(instance=document)
    return render(request, 'documents/document_form.html', {'form': form})


# Dokumento šalinimas (tik administratoriams)
@staff_member_required
def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    document.delete()
    return redirect('document_list')
