from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название курса")
    description = models.TextField(blank=True, null=True, verbose_name="Описание курса")
    preview = models.ImageField(
        upload_to="lms/pictures", blank=True, null=True, verbose_name="Превью"
    )
    owner = models.ForeignKey(
        "users.User",
        verbose_name="Владелец",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Укажите владельца",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название урока")
    description = models.TextField(blank=True, null=True, verbose_name="Описание урока")
    preview = models.ImageField(
        upload_to="lms/pictures", blank=True, null=True, verbose_name="Превью"
    )
    video_url = models.URLField(max_length=150)
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    owner = models.ForeignKey(
        "users.User",
        verbose_name="Владелец",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Укажите владельца",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
