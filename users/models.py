from django.contrib.auth.models import AbstractUser
from django.db import models
from course.models import Stage, Subject
# Create your models here.


class User(AbstractUser):

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True, null=True)
    phone_number = models.CharField(max_length=50, verbose_name='номер телефона', blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name='город', blank=True, null=True)


class Payment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', null=True, blank=True)
    date = models.DateTimeField(verbose_name='дата')
    payed_stage = models.ForeignKey(Stage, on_delete=models.CASCADE, verbose_name='оплаченный курс')
    payed_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='оплаченный предмет')
    sum = models.PositiveIntegerField(verbose_name='сумма оплаты')
    pay_approach = models.CharField(max_length=100, verbose_name='способ оплаты')

    def __str__(self):

        return f'{self.payed_stage} {self.pay_approach}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
