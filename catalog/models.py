from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

BINDING = (
        ('мягкий', 'мягкий'),
        ('твердый', 'твердый'),
    )


class Category(models.Model):
    """
    Model representing a book catalog
    """
    name = models.CharField(max_length=200, help_text="Выбирете категорию книги (e.g. Python, Java Script, Sql etc.)")

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Language(models.Model):
    """
    Model representing a Language book
    """
    name = models.CharField(max_length=200,
                            help_text="Выберете язык на котором написана книга (e.g. English, Ukrainian, Russian etc.)")

    class Meta:
        ordering = ['name']
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text='Название издательства')

    class Meta:
        ordering = ['name']
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'

    def __str__(self):
        return self.name


def isbn():
    """
    Model generate field isbn for Book model
    """
    import random
    lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '3', '5', '8']
    random.shuffle(lst)
    isbn_nums = ''.join(lst)
    return isbn_nums


class Book(models.Model):
    """
    Model representing a book.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1500, help_text='Краткое описание книги')
    isbn = models.CharField('ISBN', max_length=13, default=isbn, unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">'
                                      'ISBN number</a>')
    category = models.ManyToManyField('Category', help_text='Выбирете категорию книги')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)
    pub_year = models.PositiveSmallIntegerField(null=True, blank=True)
    num_page = models.PositiveSmallIntegerField(null=True, blank=True)
    binding = models.CharField(max_length=10, choices=BINDING, default='мягкий')
    # TODO add image and format

    class Meta:
        ordering = ['title']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        permissions = (('has_the_right_to_edit', 'Can edit book'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_category(self):
        """
        Creates a string to display the catalog in Admin.
        """
        return ', '.join([category.name for category in self.category.all()[:3]])
    display_category.short_description = 'Category'


class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, default='biography')
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    # TODO add image

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.first_name)

