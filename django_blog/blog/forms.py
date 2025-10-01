from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post   # 👈 import Post model


# update user info
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


# update extra profile fields
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']


# registration form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# blog post form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]  # user can only set title & content
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter post title"
            }),
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 6,
                "placeholder": "Write your blog content here..."
            }),
        }
