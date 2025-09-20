from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    isbn=models.CharField(max_length=13,unique=True)
    published_date=models.DateField()
    available_copies=models.PositiveIntegerField(default=1)

    added_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author}"

class BorrowedBook(models.Model): 
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="borrowed")
    borrowed_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="borrowed_books")
    
    def __str__ (self): 
        return f"{self.book} is borrowed by {self.borrowed_by.username}"



