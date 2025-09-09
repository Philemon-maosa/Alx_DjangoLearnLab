from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    language = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.title} by {self.author}"


class CustomUser(AbstractUser):
    """
    A custom user model to extend the built-in Django user model.
    This model allows us to add custom fields to the user profile
    that are relevant to our application's needs.
    """
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        help_text="The user's date of birth."
    )
    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        null=True,
        blank=True,
        help_text="A profile photo for the user."
    )

    # Adding custom fields to the user model does not require
    # a new migration. We will handle that next.

    def __str__(self):
        return self.username

