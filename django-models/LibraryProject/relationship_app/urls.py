from django.urls import path
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

urlpatterns = [
    path("admin-view/", admin_view, name="admin_view"),
    path("librarian-view/", librarian_view, name="librarian_view"),
    path("member-view/", member_view, name="member_view"),
]
