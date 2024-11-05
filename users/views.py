from rest_framework import viewsets, generics

from users.models import User
from users.serializers import UserSerializer


# Create your views here.

class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()