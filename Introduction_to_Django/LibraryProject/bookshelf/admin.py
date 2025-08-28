from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('title', 'author', 'published_date')  
    
    # Add filters for easier browsing
    list_filter = ('author', 'published_date')
    
    # Enable search by title or author
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)