from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from subject.models import *


class PupilTest(TestCase):
    def setUp(self) -> None:
        self.teacher = User.objects.create_user(username='aliya',password='aliya.123456')
        self.subject = Subject.objects.create(title='math',teacher=self.teacher)
        self.pupil = Pupil.objects.create(name='pupil1',avg_score=3.5)
        self.pupil.subject.add(self.subject)

    def test_pupil_page(self):
        self.url = reverse('pupils', args=(self.subject.id,))
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code,200)


class PupilsDetailTest(TestCase):
    def setUp(self) -> None:
        self.url = reverse('pupils_detail')
        self.teacher = User.objects.create_user(username='aliya',password='123456.aliya')
        self.subjects = Subject.objects.create(title='Math',teacher=self.teacher)
        self.pupils = Pupil.objects.create(name='pupil1',avg_score=3.5)
        self.pupils.subject.add(self.subjects)
    def test_pupilsdetailpage(self):
        self.client.login(username='aliya',password='123456.aliya')
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code,200)


class PupilDetailTest(TestCase):
    def setUp(self) -> None:
        self.teacher = User.objects.create_user(username='aliya', password='123456.aliya')
        self.subjects = Subject.objects.create(title='Math', teacher=self.teacher)
        self.pupil = Pupil.objects.create(name='pupil1',avg_score=3.5)
        self.subjects_of_pupil = self.pupil.subject.add(self.subjects)
        self.scores = Score.objects.create(subject=self.subjects,pupil=self.pupil,score=5)

    def test_pupildetailpage(self):
        self.url = reverse('pupil_detail', args=(self.pupil.id,))
        self.client.login(username='aliya',password='123456.aliya')
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code,200)




