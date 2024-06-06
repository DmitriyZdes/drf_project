from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Stage, Subject, Subscription
from users.models import User

class SubjectTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="user@example.com")
        self.stage = Stage.objects.create(name="Физика", description="Естественная наука")
        self.lesson = Subject.objects.create(name="Урок_1", description="Введение", stage=self.stage, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subject_retrieve(self):
        url = reverse("course:get_course", args=(self.subject.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), self.subject.name
        )

    def test_subject_create(self):
        url = reverse("course:create_course")
        data = {
            "title": "Урок 2"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Subject.objects.filter(title="Урок_1").count(), 1
        )

    def test_subject_update(self):
        url = reverse("course:update_course", args=(self.subject.pk,))
        data = {
            "title": "Урок_10"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "Урок_10"
        )

    def test_subject_delete(self):
        url = reverse("course:delete_course", args=(self.subject.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Subject.objects.all().count(), 0
        )

    def test_subject_list(self):
        url = reverse("course:course_list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="user@example.com")
        self.stage = Stage.objects.create(name="Русский язык", description="Важно знать", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscribe(self):
        url = reverse("course:subscription_appearance")
        data = {"stage": self.stage.pk}
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {"message": "подписка добавлена"})

    def test_unsubscribe(self):
        url = reverse("course:subscription_appearance")
        data = {"stage": self.stage.pk}
        Subscription.objects.create(stage=self.stage, user=self.user)
        response = self.client.post(url,data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {'message': 'подписка удалена'})
