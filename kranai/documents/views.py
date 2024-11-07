from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Document
from .forms import DocumentForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


@login_required
def document_list(request):
    #Tik administratoriai matys visus dokumentus, kiti matys tik savo
    if request.user.is_staff:
        documents = Document.objects.all()
    else:
        documents = Document.objects.filter(created_by=request.user)
    return render(request, 'documents/document_list.html', {'documents': documents})


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


@staff_member_required
def document_delete(request, pk):
    document = get_object_or_404(document, pk=pk)
    document.delete()
    return redirect('document_list')