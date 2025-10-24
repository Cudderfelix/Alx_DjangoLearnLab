CRUD Operations for Book Model
1. Create a Book Instance
Python Command
from your_app_name.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print("Created book:", book)

Expected Output
# Created book: 1984

2. Retrieve the Book Instance
Python Command
from your_app_name.models import Book
retrieved_book = Book.objects.get(title="1984")
print("Retrieved book:", retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)

Expected Output
# Retrieved book: 1984 George Orwell 1949

3. Update the Book Title
Python Command
from your_app_name.models import Book
retrieved_book = Book.objects.get(title="1984")
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print("Updated book:", retrieved_book.title)

Expected Output
# Updated book: Nineteen Eighty-Four

4. Delete the Book Instance
Python Command
from your_app_name.models import Book
retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")
retrieved_book.delete()
print("Book deleted. Checking remaining books:")
print(Book.objects.all())

Expected Output
# Book deleted. Checking remaining books:
# <QuerySet []>
