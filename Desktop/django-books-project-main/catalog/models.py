from django.db import models

# Модель 1: Автор
class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя автора")

    def __str__(self):
        return self.name

# Модель 2: Книга
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    # НОВАЯ СТРОКА:
    external_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title