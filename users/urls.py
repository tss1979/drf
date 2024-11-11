from django.urls import path

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, PaymentListAPIView, UserDestroyAPIView, UserCreateAPIView, UserListAPIView, \
    UserRetrieveAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name


urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user-view'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),
    path('create/', UserCreateAPIView.as_view(), name='user-delete'),
    path('payments/', PaymentListAPIView.as_view(), name='payments-list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]