from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'


class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'category']
    template_name = 'book_form.html'
    success_url = '/books/'
