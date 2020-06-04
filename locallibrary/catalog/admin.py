from django.contrib import admin
from catalog.models import Genere, Libro, Istanza, Autore, Lingua

# Register your models here.
admin.site.register(Genere)
#admin.site.register(Libro)
#admin.site.register(Istanza)
#admin.site.register(Autore)
admin.site.register(Lingua)

class AutoreAdmin(admin.ModelAdmin):
	pass
admin.site.register(Autore,AutoreAdmin)

class LibroAdmin(admin.ModelAdmin):
	pass
admin.site.register(Libro, LibroAdmin)

class IstanzaAdmin(admin.ModelAdmin):
	pass
admin.site.register(Istanza, IstanzaAdmin)
