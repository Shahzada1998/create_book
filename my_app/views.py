from django.shortcuts import render, redirect

from .models import Book, Author
from .forms import BookForm


def home(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books': books,
        'authors': authors,
        'main_page': True
    }
    return render(request, 'home.html', context=context)


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()

    author = request.GET.get('author')
    if author is not None:
        books = Book.objects.filter(author__name__icontains=author)
    else:
        books = Book.objects.all()

    context = {
        'form': form,
        'books': books,
    }
    return render(request, 'create_book.html', context)
