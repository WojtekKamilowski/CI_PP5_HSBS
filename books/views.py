from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Book

# Create your views here.

# Based on Code Institue's "Boutique Ado" Walkthrough Project


def all_books(request):
    """
    Displays all books
    Includes sorting & search queries
    """

    books = Book.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('books'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            books = books.filter(queries)

    context = {
        'books': books,
        'search_term': query,
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
