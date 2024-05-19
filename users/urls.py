from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentCreateAPIView, PaymentListAPIView, PaymentRetrieveAPIView, PaymentUpdateAPIView, \
    PaymentDestroyAPIView, UserListAPIView, UserRegisterAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('payment/create/', PaymentCreateAPIView.as_view(), name='create_payment'),
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='get_payment'),
    path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='update_payment'),
    path('payment/delete/<int:pk>/', PaymentDestroyAPIView.as_view(), name='delete_payment'),
    path('users/', UserListAPIView.as_view(), name='users_list'),
    path('users/create/', UserRegisterAPIView.as_view(), name='users_create'),
    path('users/update/<int:pk>/', UserUpdateAPIView.as_view(), name='users_update'),
    path('users/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='users_destroy'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

]
