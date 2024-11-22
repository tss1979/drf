from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from school.models import Lesson, Course
from subscription.models import Subscription
from users.models import User


# Create your tests here.
class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="mail@mail.ru", password='111')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title='123')
        self.lesson = Lesson.objects.create(
            title="1",
            video_link='https://www.youtube.com/watch?111',
            course=self.course
        )

    def test_lesson_retrieve(self):
        """Тестирование просмотра одного урока"""
        url = reverse("school:lesson-one", args=(self.lesson.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("title"), self.lesson.title)

    def test_lesson_delete(self):
        """Тестирование удаления урока"""
        url = reverse("school:lesson-delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_update(self):
        """Тестирование изменения урока"""
        url = reverse("school:lesson-update", args=(self.lesson.pk,))
        data = {"title": "New Title", "video_link": "https://www.youtube.com/watch?111"}
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.all().count(), 1)
        self.assertEqual(response.json().get("title"), "New Title")

    def test_lesson_list(self):
        """Тестирование получение всех уроков"""
        url = reverse("school:lesson-list")
        response = self.client.get(url)
        result = [
            {
             'id': self.lesson.pk,
             'title': self.lesson.title,
             'description': None, 'preview': None,
             'video_link': self.lesson.video_link,
             'course': self.lesson.course.pk, 'owner': None
            }
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("count"), 1)
        self.assertEqual(response.json().get("results"), result)

    def test_lesson_create(self):
        """Тестирование создания урока"""
        url = reverse("school:lesson-create")
        data = {
            "title": "2",
            "video_link": "https://www.youtube.com/watch?111",
            "course": self.course.pk
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="mail@mail.ru", password='111')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title='123')
        self.subscription = Subscription.objects.create(
            user=self.user,
            course=self.course
        )

    def test_course_update(self):
        """Тестирование изменения курса"""
        url = reverse("school:courses-detail", args=(self.course.pk,))
        data = {"title": "New Title"}
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Course.objects.all().count(), 1)
        self.assertEqual(response.json().get("subscription"), "Subscribed")
