from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Book


class CustomUserCreationForm(UserCreationForm):
    """Form for registering a new CustomUser."""
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "date_of_birth", "profile_photo")


class CustomUserChangeForm(UserChangeForm):
    """Form for updating CustomUser details."""
    class Meta:
        model = CustomUser
        fields = ("username", "email", "date_of_birth", "profile_photo")


class BookForm(forms.ModelForm):
    """Form for creating or editing a Book instance."""
    class Meta:
        model = Book
        fields = ["title", "author", "published_date", "isbn", "pages", "language"]
