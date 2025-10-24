from django.contrib import admin

# Register your models here.
from .models import Book

admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    # 1. Columns that appear in the list view
    list_display = ("title", "author", "publication_year")

    # 2. Filters that appear on the right-hand sidebar
    list_filter = ("author", "publication_year")

    # 3. Search box - searches title and author fields
    search_fields = ("title", "author")

    # (optional) make the title column a clickable link to the change page
    list_display_links = ("title",)