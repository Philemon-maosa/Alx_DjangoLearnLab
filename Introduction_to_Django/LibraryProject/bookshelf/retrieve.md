
**retrieve.md**
```markdown
# Retrieve Book

**Command:**
```python
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author)


Django Basics Philemon
