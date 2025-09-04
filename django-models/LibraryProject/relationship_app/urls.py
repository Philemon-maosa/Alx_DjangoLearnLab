from django.urls import path
from django.contrib.auth import views as auth_views
from .views import book_list, LibraryDetailView, register

urlpatterns = [
    path("books/", book_list, name="list_books"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Auth
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", register, name="register"),
]
