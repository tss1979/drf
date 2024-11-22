from django.urls import path
from subscription.apps import SubscriptionConfig
from subscription.views import SubscriptionCreateAPIView

app_name = SubscriptionConfig.name


urlpatterns = [
    path('create/', SubscriptionCreateAPIView.as_view(), name='sub-create'),
    path('delete/', SubscriptionCreateAPIView.as_view(), name='sub-delete'),
]
