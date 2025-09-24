from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    publication_year = models.IntegerField()  # Year published
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,   # If an author is deleted, their books are deleted too
        related_name="books"        # Allows reverse lookup: author.books.all()
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"