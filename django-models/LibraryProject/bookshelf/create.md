from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", published_year=1949)
print("Created book: ", book)
# Book successfully created