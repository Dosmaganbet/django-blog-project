from django.db import models

# Модель 1: Автор
class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя автора")

    def __str__(self):
        return self.name

# Модель 2: Книга
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    # Связь с автором
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name="Автор")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    
    # ВОТ ЭТУ СТРОКУ МЫ ДОБАВИЛИ (Описание книги):
    description = models.TextField(blank=True, verbose_name="Описание книги", help_text="Введите краткое содержание")

    def __str__(self):
        return self.title