from rest_framework import serializers
from .models import Book,BorrowedBook
from django.contrib.auth.models import User
class BookSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username')

    class Meta: 
        model=Book
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model=User 
        fields=('id','username','password')

        extra_kwargs={
            'password':{'write_only':True,'required':True}
        }
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        return user
class BorrowedBookSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    borrowed_by = serializers.ReadOnlyField(source='borrowed_by.username')
    total_borrows = serializers.IntegerField(read_only=True)

    class Meta:
        model = BorrowedBook
        fields = '__all__'

class MostBorrowedBooksSerializer(serializers.ModelSerializer):
    
    added_by = serializers.ReadOnlyField(source='added_by.username')
    total_borrows = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = Book
        fields = '__all__'