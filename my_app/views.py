from django.shortcuts import render

from .models import Book


def home(request):
    books = Book.objects.all()
    context = {
        'books': books,
        'main_page': True
    }
    return render(request, 'home.html', context=context)


def create_book(request):
    author = request.GET.get('author')
    if author is not None:
        books = Book.objects.filter(author__name__icontains=author)
    else:
        books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'create_book.html', context)


