from django.test import TestCase
from django.urls import reverse
from .models import *


class HomepageTest(TestCase):
    def setUp(self) -> None:
        self.url = reverse('home')
        self.user = User.objects.create_user(username='aliya', password='123456')

    def test_homepage(self):
        self.client.login(username='aliya', password='123456')
        self.response = self.client.post(self.url)
        self.assertEqual(self.response.status_code, 200)


class SubjectpageTest(TestCase):
    def setUp(self) -> None:
        self.url = reverse('subjects')
        self.teacher = User.objects.create(username='aliya', password='aliya.123456')
        self.subjects = Subject.objects.create(title='Math', teacher=self.teacher)

    def test_subject_page(self):
        self.client.login(username='aliya', password='aliya.123456')
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)


class ScoreTest(TestCase):
    def setUp(self) -> None:
        self.teacher = User.objects.create_user(username='aliya', password='aliya.1234')
        self.subject = Subject.objects.create(title='Math', teacher=self.teacher)
        self.pupil = Pupil.objects.create(name='pupil1', avg_score=3.5)
        self.pupil.subject.add(self.subject)
        self.scores = Score.objects.create(subject=self.subject, pupil=self.pupil, score=5)

    def test_score_page(self):
        self.url = reverse('scores', args=(self.pupil.id, self.subject.id,))
        data = {
            'score': 4,
        }
        self.client.login(username='aliya', password='aliya.1234')
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, 200)

    # def test_score_page_without_login_(self):
    #     self.url = reverse('scores', args=(self.pupil.id, self.subject.id,))
    #     data = {
    #         'score': 4,
    #     }
    #     self.response = self.client.post(self.url, data)
    #     print(self.response.content)
    #     self.assertContains(self.response,text='Login please')

    def test_score_page_bad_score_value_bigger(self):
        self.url = reverse('scores', args=(self.pupil.id, self.subject.id,))
        data = {
            'score': 10,
        }
        self.client.login(username='aliya', password='aliya.1234')
        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response,form='form',field='score',errors='Ensure this value is less than or equal to 5.')

    def test_score_page_bad_score_value_smaller(self):
        self.url = reverse('scores', args=(self.pupil.id, self.subject.id,))
        data = {
            'score': 1,
        }
        self.client.login(username='aliya', password='aliya.1234')
        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response,form='form',field='score',errors='Ensure this value is greater than or equal to 2.')

    def test_score_page_bad_score_value_str(self):
        self.url = reverse('scores', args=(self.pupil.id, self.subject.id,))
        data = {
            'score': 'asd',
        }
        self.client.login(username='aliya', password='aliya.1234')
        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response,form='form',field='score',errors='Enter a whole number.')

