from rest_framework import serializers
from .models import Author, Book
from datetime import date

# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    """Serializes all Book fields with validation for publication_year."""
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """Ensures publication_year is not in the future."""
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for Author model with nested books
class AuthorSerializer(serializers.ModelSerializer):
    """Serializes Author name and their related books using BookSerializer."""
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
