from django.db import models
from django.db import models

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.TextField('Main Office Address', max_length=100)
	city = models.CharField(max_length=30)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']

class Author(models.Model):
	first_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=40, blank=True)
	email = models.EmailField(blank=True, verbose_name='e-mail')

	def __unicode__(self):
		return u'{} {}'.format(self.first_name, self.last_name)

class Book(models.Model):
	title = models.CharField('Title of the Book', max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField('Date of Publication', null=True, blank=True)

	def __unicode__(self):
		return self.title