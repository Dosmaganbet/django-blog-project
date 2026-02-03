from django.contrib import admin
from .models import Author, Book

# 1. Регистрация Автора
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

# 2. Регистрация Книги (ОБНОВЛЕННАЯ)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Мы добавили 'description' в конец этой строки:
    list_display = ('title', 'author', 'published_date', 'description') 
    
    # Фильтры и поиск (оставляем как было)
    list_filter = ('author', 'published_date')
    search_fields = ('title',)