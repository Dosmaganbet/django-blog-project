from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    # Достаем имя автора для удобства в API
    author_name = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Book
        # Обязательно 'Meta', а не что-то другое
        fields = ['id', 'title', 'author', 'author_name', 'description', 'published_date']