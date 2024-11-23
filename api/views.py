from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .models import Book, BorrowedBook
from .serializers import BookSerializer, BorrowedBookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import now, timedelta

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()


class BorrowBookView(APIView):
    def post(self, request, book_id):
        user = request.user
        if user.borrowed_books.filter(returned=False).count() >= 5:
            return Response({"detail": "Borrow limit exceeded."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            book = Book.objects.get(id=book_id, is_available=True)
            due_date = now() + timedelta(days=14)
            BorrowedBook.objects.create(user=user, book=book, due_date=due_date)
            book.is_available = False
            book.save()
            return Response({"detail": "Book borrowed successfully."})
        except Book.DoesNotExist:
            return Response({"detail": "Book not available."}, status=status.HTTP_404_NOT_FOUND)

class ReturnBookView(APIView):
    def post(self, request, borrow_id):
        try:
            borrow = BorrowedBook.objects.get(id=borrow_id, user=request.user, returned=False)
            borrow.returned = True
            borrow.book.is_available = True
            borrow.book.save()
            borrow.save()
            return Response({"detail": "Book returned successfully.", "overdue fine": borrow.overdue_fine()})
        except BorrowedBook.DoesNotExist:
            return Response({"detail": "Borrow record not found."}, status=status.HTTP_404_NOT_FOUND)

