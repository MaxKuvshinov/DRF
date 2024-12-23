from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson, Subscription
from users.models import User
from django.urls import reverse


class LessonApiTestCase(APITestCase):
    """Класс для тестирования уроков"""

    def setUp(self):
        self.user = User.objects.create(email="usertest@sky.pro")
        self.course = Course.objects.create(
            title="Программирование", description="Интересный курс", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title="Django Часть 1",
            description="Введение",
            video_url="https://www.youtube.com/watch?v=w-ITLbRfhnA&t=180s&ab_channel=PythonHubStudio",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("lms:lesson-retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_lesson_create(self):
        url = reverse("lms:lesson-create")
        data = {
            "title": "Django Часть 2",
            "description": "Практическая часть",
            "video_url": "https://www.youtube.com/watch?v=km6tGZ3OHvQ&ab_channel=PythonHubStudio",
            "course": self.course.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("lms:lesson-update", args=(self.lesson.pk,))
        data = {
            "title": "Теория",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Теория")

    def test_lesson_delete(self):
        url = reverse("lms:lesson-delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("lms:lesson-list")
        response = self.client.get(url)
        data = response.json()
        #print(response.json())
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "title": self.lesson.title,
                    "description": self.lesson.description,
                    "preview": None,
                    "video_url": self.lesson.video_url,
                    "course": 3,
                    "owner": 3,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_subscription(self):
        url = reverse("lms:subscription")
        course_id = self.course.id
        response = self.client.post(url, {"course_id": course_id})
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_201_CREATED])
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())
