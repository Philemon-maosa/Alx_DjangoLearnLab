from django.contrib import admin
from .models import Book, CustomUser


class BookAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for easier browsing
    list_filter = ('author', 'published_date')
    
    # Enable search by title or author
    search_fields = ('title', 'author')
    
    # Custom method to extract year from published_date
    def publication_year(self, obj):
        return obj.published_date.year
    publication_year.admin_order_field = 'published_date'  # allow sorting by date
    publication_year.short_description = 'Publication Year'


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')
    search_fields = ('username', 'email')


# Register models
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
