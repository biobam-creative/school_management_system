from django.shortcuts import render
from .models import Book


def elibrary(request):
    jss1_books = Book.objects.filter(book_class=1)
    return render(request, 'e_library/elibrary.html', {'jss1_books': jss1_books})
