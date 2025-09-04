from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.http import HttpResponse
from .models import Book, Library



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


# User registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after registering
            return redirect("list_books")  # redirect after success
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# Role check helpers
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"


def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"


def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"


# Admin View
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome Admin! You have full control.")


# Librarian View
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome Librarian! You can manage books and libraries.")


# Member View
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome Member! You can browse books.")


# ---------------------------
#  Permission-protected Book Views
# ---------------------------

# Add Book
@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author_id")  # pass author_id from form
        if title and author_id:
            Book.objects.create(title=title, author_id=author_id)
            return HttpResponse("✅ Book added successfully!")
    return HttpResponse("Use POST with 'title' and 'author_id' to add a book.")


# Edit Book
@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        new_title = request.POST.get("title")
        if new_title:
            book.title = new_title
            book.save()
            return HttpResponse(f"✅ Book updated to '{book.title}'")
    return HttpResponse("Use POST with 'title' to update a book.")


# Delete Book
@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return HttpResponse("❌ Book deleted successfully!")
