from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from .views import LoginView, LogoutView

app_name = 'relationship_app'

urlpatterns = [
    # Function-based view: List all books
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # --- Authentication URLs ---
    path ('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path ('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path ('register/', views.register, name='register'),

    # -- ROLE-BASED VIEWS ---
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    # --- CUSTOM PERMISSION URLs ---
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]