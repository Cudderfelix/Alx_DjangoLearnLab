from relationship_app.models import Book
retrieved_book = Book.objects.get(title="1984")
print("Retrieved book:", retrieved_book.title, retrieved_book.author, retrieved_book.published_year)
