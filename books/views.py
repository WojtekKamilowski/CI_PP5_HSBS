from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.

# Based on Code Institue's "Boutique Ado" Walkthrough Project


def all_books(request):
    """
    Displays all books
    """

    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'books/books.html', context)


def book_detail(request, book_id):
    """
    Books view to display details of a single book
    """

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'books/book_detail.html', context)
