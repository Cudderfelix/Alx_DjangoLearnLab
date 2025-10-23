from bookshelf.models import Book
retrieved_book = Book.objects.get(title="1984")
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print("Updated book:", retrieved_book.title)
