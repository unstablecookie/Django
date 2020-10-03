from django.db import models
from django.urls import reverse
from rest_framework import serializers
import uuid

# Create your models here.

class Genre(models.Model):
	name = models.CharField(max_length=200,help_text='enter a book genre (e.g. Science Fiction)')
	def __str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('Author', on_delete = models.SET_NULL, null = True)
	summary = models.TextField(max_length=1000,help_text = 'description of the book')
	isbn = models.CharField('ISBN',max_length=13,help_text= '13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	genre = models.ManyToManyField(Genre,help_text = 'select genre for this book')
	lang = models.ForeignKey('Language',on_delete = models.SET_NULL, null = True)
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('app1:book-detail', args=[str(self.id)])
	def display_genre(self):
		return ', '.join(genre.name for genre in self.genre.all()[:3])
	display_genre.short_description = 'Genre'

class bookSerializer(serializers.ModelSerializer):
	MESSAGE_TYPE = 'book'
	VERSION = 1
	KEY_FIELD = 'title'

	class Meta:
		model = Book
		fields = ['title']
	@classmethod
	def lookup_instance(cls, title, **kwargs):
		try:
			return Book.object.get(title=title)
		except models.Book.DoesNotExist:
			pass



class BookInstance(models.Model):
	id = models.UUIDField(primary_key = True,default = uuid.uuid4,help_text='Unique ID for this particular book across whole library')
	book = models.ForeignKey('Book', on_delete = models.SET_NULL, null = True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null = True, blank = True)

	LOAD_STATUS = (
		('m', 'Maintanance'),
		('o', 'On loan'),
		('a','Available'),
		('r','Reserved'),
		)
	status = models.CharField(
		max_length=1,
		choices = LOAD_STATUS,
		blank = True,
		default = 'm',
		help_text='Book avalability',)
	class Meta:
		ordering = ['due_back']

	def __str__(self):
		return f'{self.id} ({self.book.title})'

class Author(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null = True,blank = True)
	date_of_death = models.DateField('Died', null = True, blank = True)

	class Meta:
		ordering = ['last_name','first_name']
	def get_absolute_url(self):
		return reverse('app1:author-detail',args=[str(self.id)])
	def __str__(self):
		return f'{self.last_name},{self.first_name}'

class Language(models.Model):
	lang_id = models.CharField(max_length=100)
	def __str__(self):
		return self.lang_id

