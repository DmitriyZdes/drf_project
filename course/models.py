from django.db import models
# Create your models here.


class Stage(models.Model):

    name = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(upload_to='media/course/stage', verbose_name='картинка', null=True, blank=True)
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец курса',
                              blank=True, null=True)
    objects = models.Manager()

    def __str__(self):

        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Subject(models.Model):

    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(upload_to='media/course/subject', verbose_name='превью', null=True, blank=True)
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец урока',
                              blank=True, null=True)
    link = models.URLField(max_length=200, verbose_name='ссылка на видео', null=True, blank=True)

    objects = models.Manager()

    def __str__(self):

        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'


class Subscription(models.Model):

    objects = models.Manager()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='пользователь', blank=True, null=True)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, null=True, blank=True)
    is_subscribed = models.BooleanField(default=False, verbose_name='Признак подписки')

    def __str__(self):
        return f'{self.user}: ({self.stage})'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'