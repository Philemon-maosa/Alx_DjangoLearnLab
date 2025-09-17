from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# ViewSet for handling CRUD on Book
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()            # all Book records
    serializer_class = BookSerializer        # use your serializer
