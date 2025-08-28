# Create Book

**Command:**
```python
from bookshelf.models import Book

book = Book.objects.create(
    title="Django Basics",
    author="George Orwell",
    pages=200,
    published_date="2025-08-28"
)
print(book)


<Book: Django Basics by Philemon>
