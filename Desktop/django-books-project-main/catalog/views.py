from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# --- САЙТ ---

# 1. Главная страница
def index(request):
    books = Book.objects.all()
    return render(request, 'catalog/index.html', {'books': books})

# 2. Страница деталей книги
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'catalog/book_detail.html', {'book': book})

# 3. Страница "О нас" (ЧЕТВЕРТЫЙ ШАБЛОН)
def about(request):
    return render(request, 'catalog/about.html')


# --- API ---

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer