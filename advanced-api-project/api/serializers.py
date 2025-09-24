from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"   # includes title, publication_year, author

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # related_name="books" from models

    class Meta:
        model = Author
        fields = ["name", "books"]
