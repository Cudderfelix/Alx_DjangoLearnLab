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

# bookshelf/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile, Book, Library, Author


# --- CUSTOM USER ADMIN ---
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'date_of_birth', 'is_staff')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)


# --- REGISTER MODELS ---
admin.site.register(CustomUser, CustomUserAdmin)   # REQUIRED LINE
admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Author)