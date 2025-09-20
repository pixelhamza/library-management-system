from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomObtainAuthToken.as_view(), name='login'),

    #this for routing the crud endpoints
    path('books/',views.BookListCreate.as_view(),name='book-create-get'),
    path('books/<int:pk>/',views.BookGetUpdateDelete.as_view(),name ='book-update-del'),
]