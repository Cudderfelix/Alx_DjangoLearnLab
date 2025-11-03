# bookshelf/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Book, CustomUser


# --- BOOK VIEWS WITH PERMISSIONS ---
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        year = request.POST.get('publication_year')
        Book.objects.create(title=title, author=author, publication_year=year)
        return redirect('bookshelf:book_list')
    return render(request, 'bookshelf/book_form.html', {'action': 'Create'})


@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('bookshelf:book_list')
    return render(request, 'bookshelf/book_form.html', {'book': book, 'action': 'Edit'})


@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('bookshelf:book_list')
    return render(request, 'bookshelf/book_delete.html', {'book': book})


# --- REGISTRATION ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('bookshelf:book_list')
    else:
        form = UserCreationForm()
    return render(request, 'bookshelf/register.html', {'form': form})