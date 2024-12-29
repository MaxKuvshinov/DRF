from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from users.models import User


@shared_task
def send_course_update_email(email):
    """Рассылка на почту при обновлении курса"""
    send_mail('Обновление курса.', 'Ваш курс был обновлен.', from_email=EMAIL_HOST_USER, recipient_list=[email])


@shared_task
def blocked_inactive_user(user_id):
    """Блокировка пользователя, если он не заходил более 30 дней."""
    one_month_ago = timezone.now() - timezone.timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago, is_activ=True)

    for user in inactive_users:
        user.is_active = False
        user.save()
