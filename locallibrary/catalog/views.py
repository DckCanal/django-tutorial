from django.shortcuts import render
from .models import Autore,Libro,Istanza,Genere
from django.views import generic

# Create your views here.

def index(request):
    """Vista per la pagina index."""

    n_libri = Libro.objects.all().count()
    n_istanze = Istanza.objects.all().count()

    n_ist_disp = Istanza.objects.filter(stato__exact='d').count()

    n_autori = Autore.objects.count() #all() può essere sottinteso

    n_genere_an = Genere.objects.filter(nome__icontains='an').count()

    n_libri_la = Libro.objects.filter(titolo__contains='La').count()#è comunque case-insensitive...???



    c = {
        'n_libri':n_libri,
        'n_istanze':n_istanze,
        'n_disponibili':n_ist_disp,
        'n_autori':n_autori,
        'n_an':n_genere_an,
        'n_la':n_libri_la
    }

    return render(request,'index.html',context = c)


class BookListView(generic.ListView):
    model = Libro
    context_object_name = 'elenco_libri'
    #queryset = Libro.objects.filter(titolo__contains='Il')
    #template_name = 'pattern/template_personalizzato.html'
    #template di default: /locallibrary/catalog/templates/catalog/libro_list.html

    #def get_queryset(self):
    #   return Libro.object.all()[:5]

    def get_context_data(self, **kwargs):
        #Prima richiamo la funzione base
        context = super(BookListView,self).get_context_data(**kwargs)
        #Poi aggiungo i dati che voglio io
        context['VariabileCiullosa'] = 'Ciurillini' + 3
        return context  