from django.core.management.base import BaseCommand
from django.utils import timezone

from lms.models import Course, Lesson
from users.models import Payments


class Command(BaseCommand):
    help = "Заполнение таблицы Payment данными"

    def handle(self, *args, **options):
        course1 = Course.objects.get(id=1)
        lesson1 = Lesson.objects.get(id=1)

        sample_data = [
            {
                "user_id": 1,
                "payment_date": timezone.now(),
                "paid_course": course1,
                "paid_lesson": None,
                "payment_amount": 5000.00,
                "payment_method": "cash",
            },
            {
                "user_id": 2,
                "payment_date": timezone.now(),
                "paid_course": None,
                "paid_lesson": lesson1,
                "payment_amount": 2000.00,
                "payment_method": "transfer",
            },
        ]

        for item in sample_data:
            Payments.objects.create(**item)
        self.stdout.write(self.style.SUCCESS("Данные успешно загружены!"))
