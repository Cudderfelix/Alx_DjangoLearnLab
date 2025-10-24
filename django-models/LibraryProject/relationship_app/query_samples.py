# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    """
    author = Author.objects.get(name=author_name)
    # REQUIRED: filter via Book model
    books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books:
        print(f"  - {book}")


def list_books_in_library(library_name):
    """
    List all books in a library.
    """
    library = Library.objects.get(name=library_name)   # REQUIRED
    books = library.books.all()
    print(f"Books in '{library_name}':")
    for book in books:
        print(f"  - {book}")


def get_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    """
    library = Library.objects.get(name=library_name)
    # REQUIRED: query Librarian via library field
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for '{library_name}': {librarian}")


# Sample data + execution
if __name__ == "__main__":
    if not Author.objects.exists():
        a1 = Author.objects.create(name="George Orwell")
        a2 = Author.objects.create(name="J.K. Rowling")
        b1 = Book.objects.create(title="1984", author=a1)
        b2 = Book.objects.create(title="Animal Farm", author=a1)
        b3 = Book.objects.create(title="Harry Potter", author=a2)

        lib = Library.objects.create(name="Central Library")
        lib.books.add(b1, b2, b3)

        Librarian.objects.create(name="Alice Johnson", library=lib)

    query_books_by_author("George Orwell")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")