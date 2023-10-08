import os
from xhtml2pdf import pisa
from django.http import HttpResponse, HttpResponseRedirect
from io import BytesIO
from django.shortcuts import render
from django.http import FileResponse
from PyPDF2 import PdfWriter, PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.template.loader import get_template
from django.http import HttpResponse
from django.template.loader import get_template
import reportlab
from django.conf import settings
from xhtml2pdf.files import pisaFileObject
from django.template import loader

from .forms import DemandeDeSalleForm,DemandeEvenementForm
from .models import مطلب_حجز_قاعة,بيانات_النادي
from django.template.loader import render_to_string
from django.utils import timezone


def index(request):
    return render(request, 'clubapp/home.html')


def demandeDeSalle(request):
    if request.method == "POST":
        form = DemandeDeSalleForm(request.POST, request.FILES)
        if form.is_valid():
            form_instance = form.save()
            list = مطلب_حجز_قاعة.objects.get(id=form_instance.id)
            current_date = timezone.now().date()
            formatted_date = current_date.strftime('%d/%m/%Y')
            list.اليوم_و_التوقيت = list.اليوم_و_التوقيت.strftime('%H:%M - %d/%m/%Y ')
            context = {'list': list, 'date': formatted_date}
            open('clubapp/templates/temp/demandeSalle.html', "w",encoding='utf-8').write(render_to_string('htmlfiles/demandeSalle.html',context))
            return CreatePDF('temp/demandeSalle.html')
    else:
        form = DemandeDeSalleForm()
    form.fields['القاعة'].choices = [
        (value, label) for value, label in form.fields['القاعة'].choices if value]
    form.fields['اسم_النادي_أو_المنظمة'].choices = [
        (value, label) for value, label in form.fields['اسم_النادي_أو_المنظمة'].choices if value]
    return render(request, 'clubapp/demande-de-salle.html', {'form': form})

def demandeEvenement(request):
    if request.method == "POST":
        form = DemandeEvenementForm(request.POST, request.FILES)
        if form.is_valid():
            form_instance = form.save()
            list = مطلب_نشاط.objects.get(id=form_instance.id)
            current_date = timezone.now().date()
            formatted_date = current_date.strftime('%d/%m/%Y')
            list.الزمان = list.الزمان.strftime('%H:%M - %d/%m/%Y ')
            context = {'list': list, 'date': formatted_date}
            open('clubapp/templates/temp/demandeEvenement.html',"w",encoding='utf-8').write(render_to_string('htmlfiles/demandeEvenement.html',context))
            return CreatePDF('temp/demandeEvenement.html')
    else:
        form = DemandeEvenementForm()
    form.fields['اسم_النادي'].choices = [
        (value, label) for value, label in form.fields['اسم_النادي'].choices if value]
    return render(request, 'clubapp/demandeEvenement.html', {'form': form})

def requests(request):
    return render(request, 'clubapp/requests.html')


def CreatePDF(template_name):
    PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
    existing_pdf = os.path.join(PROJECT_DIR, 'club.pdf')
    # generate pdf
    file = BytesIO()
    pdf_reader = PdfReader(open(existing_pdf, "rb"))
    pdf_writer = PdfWriter()

    page = pdf_reader.pages[0]

    # convert html to pdf
    template = get_template(template_name)
    template_content = template.render()
    pisaFileObject.getNamedFile = lambda self: self.uri
    pdf = pisa.CreatePDF(BytesIO(template_content.encode('utf-8')), file)
    new_pdf = PdfReader(file)

    new_page = new_pdf.pages[0]
    page.merge_page(new_page)
    pdf_writer.add_page(page)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Demande de salle.pdf"'

    output = BytesIO()
    pdf_writer.write(output)
    pdf_data = output.getvalue()
    response.write(pdf_data)
    if not pdf.err:
        return response
    return None


#page-admin
def clubsView (request):
    clubs_list = بيانات_النادي.objects.all()
    return render(request, 'admin/clubs.html', {'clubs': clubs_list})
def ListDemmandes(request,id):
    return render(request,'admin/listDemmandes.html',{'id':id})
def DemmSalle(request,id):
    club = بيانات_النادي.objects.get(id=id)
    list = مطلب_حجز_قاعة.objects.filter(اسم_النادي_أو_المنظمة=club)
    for i in list:
        i.اليوم_و_التوقيت = i.اليوم_و_التوقيت.strftime('%d/%m/%Y - %H:%M ')
    return render(request,'admin/demandeSalle.html',{'list':list})   
def DemmEven(request,id):
    club = بيانات_النادي.objects.get(id=id)
    list = مطلب_نشاط.objects.filter(اسم_النادي=club)
    return render(request,'.html',{'list':list})
    