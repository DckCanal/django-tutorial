from django.shortcuts import render
from django.views import generic
from .models import Autore, Libro, Istanza, Genere
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.


def index(request):
    """Vista per la pagina index."""

    n_libri = Libro.objects.all().count()
    n_istanze = Istanza.objects.all().count()

    n_ist_disp = Istanza.objects.filter(stato__exact='d').count()

    n_autori = Autore.objects.count()  # all() può essere sottinteso

    n_genere_an = Genere.objects.filter(nome__icontains='an').count()

    n_libri_la = Libro.objects.filter(titolo__contains='La').count()
    # è comunque case-insensitive...???
    pref = request.session.get('libro_preferito', None)
#    if pref:
#        libro_preferito = Libro.objects.filter(id__exact=pref)
#    else:
#        libro_preferito = None

    num_visit = request.session.get('num_visit', 0)
    request.session['num_visit'] = num_visit+1

    cont = {
        'n_libri': n_libri,
        'n_istanze': n_istanze,
        'n_disponibili': n_ist_disp,
        'n_autori': n_autori,
        'n_an': n_genere_an,
        'n_la': n_libri_la,
        'num_visit': num_visit,
        # 'libro_preferito': libro_preferito,
    }

    return render(request, 'index.html', context=cont)

# class setPreferito(generic.DetailView):
#    model = Libro
#    template_name = 'templates/catalog/set_pref.html'


class BookListView(generic.ListView):
    """ListView per la classe models.Libro"""
    model = Libro
    context_object_name = 'elenco_libri'
    paginate_by = 5
    #queryset = Libro.objects.filter(titolo__contains='Il')
    #template_name = 'catalog/templates/libro_list.html'
    # template di default: /locallibrary/catalog/templates/catalog/libro_list.html

    # def get_queryset(self):
    #   return Libro.object.all()[:5]

    def get_context_data(self, **kwargs):
        # Prima richiamo la funzione base
        context = super(BookListView, self).get_context_data(**kwargs)
        # Poi aggiungo i dati che voglio io
        #context['VariabileCiullosa'] = 'Ciurillini'
        return context


class BookDetailView(generic.DetailView):
    """DetailView per la classe models.Libro"""
    model = Libro
    #template_name = 'templates/dettaglio_libro.html'


class AutoreListview(generic.ListView):
    model = Autore
    paginate_by = 5
    context_object_name = 'elenco_autori'


class AutoreDetailView(generic.DetailView):
    model = Autore


class LoanedBookByUserListView(LoginRequiredMixin, generic.ListView):
    model = Istanza
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Istanza.objects.filter(borrower=self.request.user).filter(stato__exact='p').order_by('riconsegna')

class LoanedBookByLibrarianListView(PermissionRequiredMixin, generic.ListView):
    model = Istanza
    template_name = 'catalog/bookinstance_list_borrowed_librarian.html'
    paginate_by = 10
    permission_required = 'catalog.can_mark_returned'
    
    def get_queryset(self):
        return Istanza.objects.filter(stato__exact='p').order_by('riconsegna')
