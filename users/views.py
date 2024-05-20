from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from users.serializers import PaymentSerializer, UserSerializer
from users.models import Payment, User


class PaymentCreateAPIView(CreateAPIView):

    serializer_class = PaymentSerializer


class PaymentListAPIView(ListAPIView):

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['date']
    filterset_fields = ['payed_stage', 'pay_approach']


class PaymentRetrieveAPIView(RetrieveAPIView):

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentUpdateAPIView(UpdateAPIView):

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentDestroyAPIView(DestroyAPIView):

    queryset = Payment.objects.all()


class UserRegisterAPIView(CreateAPIView):

    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateAPIView(UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDestroyAPIView(DestroyAPIView):

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
