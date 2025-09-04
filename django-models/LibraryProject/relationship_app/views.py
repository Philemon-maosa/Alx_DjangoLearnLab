from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library


# Function-based view: list all books
def book_list(request):
    books = Book.objects.all()
    if not books.exists():
        return HttpResponse("No books available.")
    
    output = "Books:<br>"
    for book in books:
        output += f"- {book.title} by {book.author.name}<br>"
    return HttpResponse(output)


# Class-based view: details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    context_object_name = "library"

    def render_to_response(self, context, **response_kwargs):
        library = context["library"]
        books = library.books.all()
        if not books.exists():
            return HttpResponse(f"Library: {library.name}<br>No books in this library.")
        
        output = f"Library: {library.name}<br>Books:<br>"
        for book in books:
            output += f"- {book.title} by {book.author.name}<br>"
        return HttpResponse(output)
