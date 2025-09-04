from django.urls import path
from .views import (
    book_list,
    LibraryDetailView,
    register,
    admin_view,
    librarian_view,
    member_view,
    add_book,
    edit_book,
    delete_book,
)

urlpatterns = [
    path("books/", book_list, name="list_books"),
    path("books/add/", add_book, name="add_book"),
    path("books/<int:book_id>/edit/", edit_book, name="edit_book"),
    path("books/<int:book_id>/delete/", delete_book, name="delete_book"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("register/", register, name="register"),
    path("admin-view/", admin_view, name="admin_view"),
    path("librarian-view/", librarian_view, name="librarian_view"),
    path("member-view/", member_view, name="member_view"),
]
