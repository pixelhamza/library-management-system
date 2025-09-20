from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics,permissions,filters,status
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from .serializers import UserSerializer,BookSerializer
from .models import Book 

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# this to handle user login and the use of token. this was  a bit new stuff for me just learned proper auth...
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        return Response({
            'token': token.key,
            'user_id': user.pk, 
            'username': user.username
        })
class StandardResultsSetPagination(PageNumberPagination):
    page_size=10
    page_query_param='page_size'
    max_page_size=100

#this handles GET to show all the books and i have implemented paginaton for ease view and filtering too 
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backend = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'category', 'isbn'] #the optional search by i implemented , lowkey easy
    ordering_fields = ['title', 'author', 'published_date', 'available_copies'] 
   
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

        
#generic api view to handle PUT,DELETE,GET.i went for generic instead of decorators cuz i thought it was more professional and industry ready
class BookGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView): 
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(added_by=self.request.user)





