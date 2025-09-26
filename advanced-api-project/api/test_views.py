from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username="tester", password="pass1234")

        # Create an author and a book
        self.author = Author.objects.create(name="Author One")
        self.book = Book.objects.create(
            title="Book One",
            publication_year=2020,
            author=self.author
        )

        # Endpoints
        self.list_url = reverse("book-list")   # /books/
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book.id})

    # ---------- CRUD TESTS ----------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_single_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Book One")

    def test_create_book_authenticated(self):
        self.client.login(username="tester", password="pass1234")
        data = {"title": "New Book", "publication_year": 2022, "author": self.author.id}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        data = {"title": "Unauthorized Book", "publication_year": 2022, "author": self.author.id}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        self.client.login(username="tester", password="pass1234")
        data = {"title": "Updated Book", "publication_year": 2021, "author": self.author.id}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        self.client.login(username="tester", password="pass1234")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # ---------- FILTER, SEARCH, ORDER ----------
    def test_filter_books_by_year(self):
        response = self.client.get(f"{self.list_url}?publication_year=2020")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_search_books_by_title(self):
        response = self.client.get(f"{self.list_url}?search=Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books_by_title(self):
        response = self.client.get(f"{self.list_url}?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
