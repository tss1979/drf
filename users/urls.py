from django.urls import path

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, PaymentListAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('payments/', PaymentListAPIView.as_view(), name='payments-list'),
]