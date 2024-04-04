from django.db import models

from users.models import User


# Create your models here.


class Stage(models.Model):

    name = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(upload_to='media/course/stage', verbose_name='картинка', null=True, blank=True)
    description = models.TextField(verbose_name='описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', null=True, blank=True)

    def __str__(self):

        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Subject(models.Model):

    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(upload_to='media/course/subject', verbose_name='превью', null=True, blank=True)
    description = models.TextField(verbose_name='описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', null=True, blank=True)

    def __str__(self):

        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'
