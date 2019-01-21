from django.shortcuts import render
from .models import Book, Author, Category
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin


class BookListView(generic.ListView):
    model = Book
    paginate_by = 20


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 15


class AuthorDetailView(generic.DetailView):
    model = Author


class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    # initial = {'date_of_death': '05/01/2018', }
    permission_required = 'has_the_right_to_edit'


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    permission_required = 'has_the_right_to_edit'


class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 'has_the_right_to_edit'


class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    # initial = {'summary': 'This book is...', }
    permission_required = 'has_the_right_to_edit'


class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    permission_required = 'has_the_right_to_edit'


class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    permission_required = 'has_the_right_to_edit'
