from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


@shared_task
def send_course_update_email(email):
    """Рассылка на почту при обновлении курса"""
    send_mail('Обновление курса.', 'Ваш курс был обновлен.', from_email=EMAIL_HOST_USER, recipient_list=[email])
