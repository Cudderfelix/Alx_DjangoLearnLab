# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian


def list_books_in_library(library_name):
    """
    List all books in a library.
    """
    library = Library.objects.get(name=library_name)  
    books = library.books.all()
    print(f"Books in '{library_name}':")
    for book in books:
        print(f"  - {book}")


def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    """
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    print(f"Books by {author_name}:")
    for book in books:
        print(f"  - {book}")



def get_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    """
    library = Library.objects.get(name=library_name)
    try:
        librarian = library.librarian
        print(f"Librarian for '{library_name}': {librarian}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")


# Sample execution (for testing)
if __name__ == "__main__":
    # Create sample data if DB is empty
    if not Author.objects.exists():
        author1 = Author.objects.create(name="George Orwell")
        author2 = Author.objects.create(name="J.K. Rowling")

        book1 = Book.objects.create(title="1984", author=author1)
        book2 = Book.objects.create(title="Animal Farm", author=author1)
        book3 = Book.objects.create(title="Harry Potter", author=author2)

        library = Library.objects.create(name="Central Library")
        library.books.add(book1, book2, book3)

        Librarian.objects.create(name="Alice Johnson", library=library)

    # Run the queries
    query_books_by_author("George Orwell")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")