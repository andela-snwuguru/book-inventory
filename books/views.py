from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
