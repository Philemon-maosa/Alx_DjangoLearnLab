# relationship_app/query_samples.py

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# -----------------------------
# Query 1: All books by a specific author using objects.filter()
# -----------------------------
def books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)  # objects.filter instead of related_name
    if books.exists():
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    else:
        print(f"No books found for author '{author_name}'")


# -----------------------------
# Query 2: List all books in a library using objects.filter()
# -----------------------------
def books_in_library(library_name):
    books = Book.objects.filter(libraries__name=library_name)  # uses ManyToMany reverse lookup
    if books.exists():
        print(f"Books in library '{library_name}':")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    else:
        print(f"No books found in library '{library_name}'")


# -----------------------------
# Query 3: Retrieve the librarian for a library using objects.filter()
# -----------------------------
def librarian_of_library(library_name):
    librarians = Librarian.objects.filter(library__name=library_name)  # OneToOneField reverse lookup
    if librarians.exists():
        librarian = librarians.first()
        print(f"Librarian of '{library_name}': {librarian.name}")
    else:
        print(f"No librarian assigned to '{library_name}' or library not found")


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    # Replace with actual names in your database
    books_by_author("J.K. Rowling")
    print("\n")
    books_in_library("Central Library")
    print("\n")
    librarian_of_library("Central Library")
