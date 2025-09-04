from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Book
from .models import Library
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse



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


#  Role check helpers
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"


def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"


def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"


#  Admin View
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome Admin! You have full control.")


#  Librarian View
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome Librarian! You can manage books and libraries.")


# Member View
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome Member! You can browse books.")

