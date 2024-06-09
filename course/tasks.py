import datetime

from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from course.models import Stage, Subscription
from users.models import User


@shared_task
def send_letter(stage_id):

    course = Stage.objects.get(pk=stage_id)
    subscribers = Subscription.objects.get(stage=stage_id)

    send_mail(subject=f'Обновление курса{course}', message=f'Уведомляем об очередном обновлении курса {course}',
              from_email=EMAIL_HOST_USER, recipient_list=[subscribers.user.email])


@shared_task
def check_user():

    active_users = User.objects.filter(is_active=True)
    now = datetime.datetime.now()

    for user in active_users:
        if user.last_login:
            if now - user.last_login > datetime.timedelta(days=30):
                user.is_active = False
                user.save()
                print(f'Пользователь {user} не активен')
