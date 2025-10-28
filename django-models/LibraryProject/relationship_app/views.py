#relationship_app/views.py
# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


# -------------------------------------------------
# 1. Function-based view – list all books (plain HTML)
# -------------------------------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# -------------------------------------------------
# 2. Class-based view – detail of a single library
# -------------------------------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    # Pre-fetch books + their authors to avoid N+1 queries
    def get_queryset(self):
        return Library.objects.prefetch_related('books__author')