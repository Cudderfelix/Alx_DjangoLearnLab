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
]