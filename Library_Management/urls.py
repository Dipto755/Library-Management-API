from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import BookViewSet, BorrowBookView, ReturnBookView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

#create router
router = DefaultRouter()
#register viewsets with router
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('borrow/<int:book_id>/', BorrowBookView.as_view(), name='borrow-book'),
    path('return/<int:borrow_id>/', ReturnBookView.as_view(), name='return-book'),
    path('get-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-token/', TokenVerifyView.as_view(), name='token_verify'),
]

