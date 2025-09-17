from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# View to list all books
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
