from django.contrib import admin
from catalog.models import Genere, Libro, Istanza, Autore, Lingua

# Register your models here.
admin.site.register(Genere)
#admin.site.register(Libro)
#admin.site.register(Istanza)
#admin.site.register(Autore)
admin.site.register(Lingua)

class AutoreAdmin(admin.ModelAdmin):
	list_display = ('cognome','nome','data_nascita','data_morte')
	
admin.site.register(Autore,AutoreAdmin)

class LibroAdmin(admin.ModelAdmin):
	list_display = ('titolo','autore','mostra_genere')
admin.site.register(Libro, LibroAdmin)

class IstanzaAdmin(admin.ModelAdmin):
	pass
admin.site.register(Istanza, IstanzaAdmin)
