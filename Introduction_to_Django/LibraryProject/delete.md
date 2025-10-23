From bookshelf.models import Book
delete_book = Book.objects.get(title="Nineteen Eighty-Four")
retrieved_book.delete()
print("Book deleted. Checking remaining books:")
print(Book.objects.all())

