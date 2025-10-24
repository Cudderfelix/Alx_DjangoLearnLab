from relationship_app.models import Author, Book, Library, librarian

def demo_queries():
   # 1 Query all books by a specific author
    author_name = "George Orwell"
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()
    print(f"\n=== Books by {author_name} ===")
    for b in books_by_author:
        print(f"- {b}")

   # 2 List all books in a specific library
   lib_name = "Central City Library"
   library = Library.objects.get(name=lib_name)
   books_in_lib = library.books.all()
   print(f"\n=== Books in {lib_name} ===")
   for b in books_in_lib:
       print(f"- {b}")          
    # 3 Find the librarian of a specific library
   print(f"\n=== Librarian for '{lib_name}' ===")
    try: 
        librarian = library.librarian
        print(f"- {librarian}")
    except librarian.DoesNotExist:
        print("- No librarian assigned.")       

if __name__ == "__name__":
# Populate a tiny dataset if the DB is empty
    if not Author.objects.exists():
        a1 = Author.objects.create(name="George Orwell")
        a2 = Author.objects.create(name="J.K. Rowling")
        b1 = Book.objects.create(title="1984", author=a1)
        b2 = Book.objects.create(title="Animal Farm", author=a1)
        b3 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=a2)

        lib = Library.objects.create(name="Central City Library")
        lib.books.set([b1, b2, b3])
        librarian.objects.create(name="Alice Johnson", library=lib) 
    demo_queries()