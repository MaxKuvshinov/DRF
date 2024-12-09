from django.contrib.auth.models import AbstractUser
from django.db import models
from lms.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Укажите email")
    avatar = models.ImageField(upload_to="users/avatars/", blank=True, null=True, verbose_name="Аватар")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон", help_text="Укажите телефон")
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город", help_text="Укажите город")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payments(models.Model):
    PAYMENT_METHOD = [("cash", "наличные"), ("transfer", "перевод на счет"),]

    user = models.ForeignKey(User, verbose_name="Пользователь", blank=True, null=True, on_delete=models.CASCADE, related_name="payment_history")
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты")
    paid_course = models.ForeignKey(Course, verbose_name="Оплаченный курс", blank=True, null=True, on_delete=models.CASCADE)
    paid_lesson = models.ForeignKey(Lesson, verbose_name="Оплаченный урок", blank=True, null=True, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма оплаты")
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD, verbose_name="Способ оплаты")

    def __str__(self):
        return f'{self.user} - {self.payment_method} - {self.payment_amount} - {self.payment_date}'

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
