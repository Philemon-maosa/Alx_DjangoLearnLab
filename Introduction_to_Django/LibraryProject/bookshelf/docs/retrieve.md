# Retrieve
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author)
# Output: Django Basics Philemon