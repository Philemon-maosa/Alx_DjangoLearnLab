from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library


# Function-based view to list all books
def book_list(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view to display details of a library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()  # all books in this library
        return context
