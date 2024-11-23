from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    is_available = models.BooleanField(default=True)
    added_at = models.DateTimeField(auto_now_add=True)

class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    returned = models.BooleanField(default=False)

    def overdue_fine(self):
        if not self.returned and now() > self.due_date:
            overdue_days = (now() - self.due_date).days
            return overdue_days * 5  # 5 BDT per day
        return 0

