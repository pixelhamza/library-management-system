from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions, filters, status
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Book, BorrowedBook
from .serializers import UserSerializer, BookSerializer, BorrowedBookSerializer,MostBorrowedBooksSerializer
from django.db.models import Count


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny] 

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        return Response({
            'token': token.key,
            'user_id': user.pk, 
            'username': user.username,
        })

class StandardResultsSetPagination(PageNumberPagination):
    page_size=10
    page_query_param='page_size'
    max_page_size=100


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
  

    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'category', 'isbn']
    ordering_fields = ['title', 'author', 'published_date', 'available_copies'] 
   
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)



class BookGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView): 
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAuthenticated]

class BorrowBook(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, format=None):
        book = get_object_or_404(Book, pk=pk)
        user = request.user
        
        if book.available_copies > 0:
            BorrowedBook.objects.create(book=book, borrowed_by=user)
            book.available_copies -= 1
            book.save()
            return Response({'message':"YEAYY!! You Borrowed the book Sucessfully"},status=status.HTTP_200_OK)
        else: 
            return Response({'message':"No Copies Available to Borrow"},status=status.HTTP_400_BAD_REQUEST)

class BorrowedBookList(generics.ListAPIView):
    serializer_class = BorrowedBookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BorrowedBook.objects.filter(borrowed_by=self.request.user)
    
    #query for most borrowed
class MostBorrowedBooksView(generics.ListAPIView):
    serializer_class=MostBorrowedBooksSerializer
    
    def get_queryset(self):
        queryset = Book.objects.annotate(
            
            total_borrows=Count('borrowed')
        ).order_by('-total_borrows')[:3]
        return queryset




