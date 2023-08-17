from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Book, Era
from .forms import BookForm


# Create your views here.

# Based on Code Institue's "Boutique Ado" Walkthrough Project


def all_books(request):
    """
    Displays all books
    Includes sorting & search queries
    """

    books = Book.objects.all()
    query = None
    eras = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                books = books.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            books = books.order_by(sortkey)

        if 'era' in request.GET:
            eras = request.GET['era'].split(',')
            books = books.filter(era__name__in=eras)
            eras = Era.objects.filter(name__in=eras)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You did not enter any search criteria!")
                return redirect(reverse('books'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            books = books.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'books': books,
        'search_term': query,
        'current_eras': eras,
        'current_sorting': current_sorting,
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


def add_book(request):
    """
    View to add a new book to the store offer
    """
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Book added successfully ')
            return redirect(reverse('book_detail', args=[book.id]))
        else:
            messages.error(request,
                           ('Failed to add book. '
                            'Please try again & ensure the form is valid.'))
    else:
        form = BookForm()

    template = 'books/add_book.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_book(request, book_id):
    """
    View to edit selected book from the store
    """
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book has been updated successfully!')
            return redirect(reverse('book_detail', args=[book.id]))
        else:
            messages.error(
                request, 'Failed to update book.'
                'Please try again & ensure the form is valid.')
    else:
        form = BookForm(instance=book)
        messages.info(request, f'You are currently editing {book.name}')

    template = 'books/edit_book.html'
    context = {
        'form': form,
        'book': book,
    }

    return render(request, template, context)
