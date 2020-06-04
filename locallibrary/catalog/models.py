from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Genere(models.Model):
	"""Modello per il genere del libro."""
	nome = models.CharField(max_length=200, help_text='Inserisci il genere (es: fantascienza)')
	
	def __str__(self):
		"""String for representing the Model object."""
		return self.nome

class Libro(models.Model):
	"""Modello per rappresentare un libro (non una copia fisica)."""
	titolo = models.CharField(max_length=200)
	sommario = models.TextField(max_length=1000, help_text='Inserisci una breve descrizione del libro.')
	isbn = models.CharField("ISBN",max_length=13, help_text='13 caratteri <a href="https://www.isbn-international.org/content/what-isbn"> ISBN </a>')
	
	genere = models.ManyToManyField(Genere, help_text="Scegli il genere per questo libro.")
	autore = models.ForeignKey('Autore', on_delete = models.SET_NULL, null=True)
	lingua = models.ForeignKey('Lingua', help_text = "Lingua", on_delete = models.SET_NULL, null=True)
	
	class Meta:
		ordering = ['titolo']
	def __str__(self):
		"""String for representing the Model object."""
		return self.titolo
	
	def get_absolute_url(self):
		"""Return the url to access a detail record for this book."""
		return reverse('book-detail',args=[str(self.id)])
		
class Istanza(models.Model):
	"""Modello che rappresenta una specifica copia di un libro, che può ad esempio essere prestata."""
	id = models.UUIDField(primary_key=True,default=uuid.uuid4, help_text="ID univoco di uno specifico libro nella biblioteca.")
	libro = models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200, help_text = "Non so cosa sia in effetti...")
	riconsegna = models.DateField(null=True, blank=True)
	
	LOAN_STATUS = (
		('m', 'Manutenzione'),
		('p', 'Prestato'),
		('d','Disponibile'),
		('r','Riservato'),
	)
	
	stato = models.CharField(
		max_length = 1,
		choices = LOAN_STATUS,
		blank = True, 
		default = 'm',
		help_text = "Disponibilità del libro",
	)
	
	class Meta:
		ordering = ['riconsegna']
	
	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.id} ({self.libro.titolo})'
		#return f'{self.libro.titolo}'

class Autore(models.Model):
	"""Modello per rappresentare l'autore."""
	nome = models.CharField(max_length=100)
	cognome = models.CharField(max_length=100)
	data_nascita = models.DateField(null=True, blank=True)
	data_morte = models.DateField('Morto', null=True, blank=True)
	
	class Meta:
		ordering = ['cognome','nome']
	
	def get_absolute_url(self):
		"""Returns the url to access a particular author instance."""
		return reverse('author-detail',args=[str(self.id)])
	
	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.cognome}, {self.nome}'
	
class Lingua(models.Model):
	"""Modello per rappresentare la lingua in cui è scritto un libro."""
	nome = models.CharField(max_length=100, help_text="Inserisci il nome di una lingua, es. inglese, italiano...")
	
	def __str__(self):
		"""String for representing the Model object."""
		return self.nome

