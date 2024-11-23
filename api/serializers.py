from rest_framework import serializers
from .models import User, Book, BorrowedBook

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_admin', 'is_member']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowedBookSerializer(serializers.ModelSerializer):
    overdue_fine = serializers.ReadOnlyField()

    class Meta:
        model = BorrowedBook
        fields = ['id', 'user', 'book', 'borrowed_at', 'due_date', 'returned', 'overdue_fine']
