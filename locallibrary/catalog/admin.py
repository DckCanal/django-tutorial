from django.contrib import admin
from catalog.models import Genere, Libro, Istanza, Autore, Lingua

# Register your models here.
admin.site.register(Genere)
#admin.site.register(Libro)
#admin.site.register(Istanza)
#admin.site.register(Autore)
admin.site.register(Lingua)

class LibroInline(admin.TabularInline):
	model = Libro
	extra = False

class AutoreAdmin(admin.ModelAdmin):
	list_display = ('cognome','nome','data_nascita','data_morte')
	fields = [('nome','cognome'),('data_nascita','data_morte')]
	inlines = [LibroInline]
admin.site.register(Autore,AutoreAdmin)

class IstanzaInline(admin.TabularInline):
	model = Istanza
	extra = False



class LibroAdmin(admin.ModelAdmin):
	list_display = ('titolo','autore','mostra_genere')
	inlines = [IstanzaInline]
admin.site.register(Libro, LibroAdmin)

class IstanzaAdmin(admin.ModelAdmin):
	list_display = ('libro','stato','riconsegna','id')
	list_filter = ('stato','riconsegna')
	exclude = ['id']
	fieldsets = (
		(None, {
			'fields': ('libro','imprint')
		}),
		('Disponibilità',{
			'fields': ('stato','riconsegna')
		})
	)
admin.site.register(Istanza, IstanzaAdmin)
