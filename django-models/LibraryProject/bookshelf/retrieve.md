# Retrieve Book

**Command:**
```python
from bookshelf.models import Book

retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author)

1984 George Orwell
