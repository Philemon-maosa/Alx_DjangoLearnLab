from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


# ---------- MODEL TESTS ----------
class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Author Test")
        self.book = Book.objects.create(
            title="Book Test",
            publication_year=2023,
            author=self.author
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Book Test")
        self.assertEqual(self.book.publication_year, 2023)
        self.assertEqual(self.book.author.name, "Author Test")


# ---------- API VIEW TESTS ----------
class BookAPITests(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(username="tester", password="pass1234")

        # Create author + book
        self.author = Author.objects.create(name="Author One")
        self.book = Book.objects.create(
            title="Book One",
            publication_year=2020,
            author=self.author
        )

        # Endpoints
        self.list_url = reverse("book-list")   # /books/
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book.id})

    # ---------- READ ----------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_single_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Book One")

    # ---------- CREATE ----------
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
        self.assertEqual(Book.objects.count(), 1)

    # ---------- UPDATE ----------
    def test_update_book_authenticated(self):
        self.client.login(username="tester", password="pass1234")
        data = {"title": "Updated Book", "publication_year": 2021, "author": self.author.id}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_update_book_unauthenticated(self):
        data = {"title": "Blocked Update", "publication_year": 2021, "author": self.author.id}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.book.refresh_from_db()
        self.assertNotEqual(self.book.title, "Blocked Update")

    # ---------- DELETE ----------
    def test_delete_book_authenticated(self):
        self.client.login(username="tester", password="pass1234")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 1)
