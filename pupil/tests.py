from django.test import TestCase
from django.urls import reverse
from .models import Pupil
from subject.models import *
# Create your tests here.


class PupilTest(TestCase):
    def setUp(self):
        self.url = reverse('pupils')
        self.user = User.objects.create(username='aliyaandabekova',password='123456')
        self.subject = Subject.objects.create(title='Информатика',teacher=self.user)
        Pupil.objects.create(name='aliya',subject=self.subject,avg_score=3.5)
    def test_pupil_get(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code,200)