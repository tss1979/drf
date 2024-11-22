from django.shortcuts import get_object_or_404

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from school.models import Course
from school.permissions import IsOwnerPermission
from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer, \
    UserViewSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import UserIsStaffPermission
from users.services import StripeManager


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserViewSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserViewSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerPermission]


class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerPermission | UserIsStaffPermission]


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_method',)
    ordering_fields = ('payment_date',)
    permission_classes = [IsAuthenticated | UserIsStaffPermission]


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        stripe = StripeManager()
        course = get_object_or_404(Course, pk=payment.course.pk)
        product = stripe.create_product(course)
        price = stripe.create_price(course.price, product)
        session_id, payment_link = stripe.create_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()
