from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import Book, Category


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

    def get_context_data(self, **kwargs):
        q = self.request.GET.get('q', '')
        category_id = self.request.GET.get('cat', '')
        context = super(BookListView, self).get_context_data(**kwargs)
        context['q'] = q
        context['category_id'] = category_id
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        category_id = self.request.GET.get('cat')
        if category_id:
            category = Category.objects.get(pk=category_id)
            return Book.objects.filter(category=category, name__contains=q)
        return Book.objects.filter(name__contains=q)


class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'category']
    template_name = 'book_form.html'
    success_url = '/books/'

