from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomObtainAuthToken.as_view(), name='login'),

    path('books/', views.BookListCreate.as_view(), name='book-create-get'),
    path('books/<int:pk>/', views.BookGetUpdateDelete.as_view(), name='book-update-del'),
  
    path('borrowed-books/', views.BorrowedBookList.as_view(), name='borrowed-books'),
    path('books/<int:pk>/borrow/', views.BorrowBook.as_view(), name="borrow-book"),
    path('most-borrowed/', views.MostBorrowedBooksView.as_view(), name='most-borrowed'),
]
