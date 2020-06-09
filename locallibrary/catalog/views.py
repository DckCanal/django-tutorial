from django.shortcuts import render
from .models import Autore,Libro,Istanza,Genere

# Create your views here.

def index(request):
    """Vista per la pagina index."""

    n_libri = Libro.objects.all().count()
    n_istanze = Istanza.objects.all().count()

    n_ist_disp = Istanza.objects.filter(stato__exact='d').count()

    n_autori = Autore.objects.count() #all() può essere sottinteso

    c = {
        'n_libri':n_libri,
        'n_istanze':n_istanze,
        'n_disponibili':n_ist_disp,
        'n_autori':n_autori,
    }

    return render(request,'index.html',context = c)