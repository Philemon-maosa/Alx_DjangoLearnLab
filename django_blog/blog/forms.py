from django import forms
from .models import Post
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=TagWidget(attrs={
        "class": "form-control",
        "placeholder": "Add tags separated by commas"
    }))

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
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
