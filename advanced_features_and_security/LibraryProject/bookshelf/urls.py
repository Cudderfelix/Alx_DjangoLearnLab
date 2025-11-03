# bookshelf/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'bookshelf'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='bookshelf/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='bookshelf/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Book URLs
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
]