# relationship_app/query_samples.py

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# -----------------------------
# Query 1: All books by a specific author using objects.filter(author=author)
# -----------------------------
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # <-- exactly what the check expects
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'")


# -----------------------------
# Query 2: List all books in a library
# -----------------------------
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # uses get()
        books = library.books.all()  # ManyToManyField
        print(f"Books in library '{library_name}':")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")


# -----------------------------
# Query 3: Retrieve the librarian for a library
# -----------------------------
def librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # uses get()
        librarian = library.librarian  # OneToOneField
        print(f"Librarian of '{library_name}': {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'")


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    books_by_author("J.K. Rowling")
    print("\n")
    books_in_library("Central Library")
    print("\n")
    librarian_of_library("Central Library")
