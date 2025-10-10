from django.db import models

# Create your models here.

class Author(models.Model):
    """Stores the author's name."""
    name = models.CharField(max_length=100, help_text="Author's full name")

    def __str__(self):
        return self.name

class Book(models.Model):
    """Stores book details with a foreign key to Author (one-to-many)."""
    title = models.CharField(max_length=200, help_text="Book title")
    publication_year = models.IntegerField(help_text="Year of publication")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', help_text="Author of the book")

    def __str__(self):
        return self.title