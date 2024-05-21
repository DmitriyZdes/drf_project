from django.contrib.auth.hashers import make_password

from users.models import Payment, User
from rest_framework import serializers


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = '__all__'
