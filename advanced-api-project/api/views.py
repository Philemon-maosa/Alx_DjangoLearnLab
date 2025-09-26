from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework   
from django_filters.rest_framework import DjangoFilterBackend 
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListCreateAPIView):
    """
    API endpoint that allows books to be listed or created.
    Supports filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Enable filter, search, and ordering backends
    filter_backends = [
        DjangoFilterBackend,   # For filtering
        filters.SearchFilter,  # For searching
        filters.OrderingFilter # For ordering
    ]

    # Allow filtering on specific fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Allow search on text-based fields
    search_fields = ['title', 'author__name']

    # Allow ordering results
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint
