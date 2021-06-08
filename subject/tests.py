# from django.test import TestCase
# from django.urls import reverse
# from .models import *
#
# # Create your tests here.
#
# class SubjectTest(TestCase):
#     def setUp(self):
#         self.url = reverse('subjects')
#         self.user = User.objects.create_user(username='aliya',password='aliya.123456')
#         Subject.objects.create(title='Математика', teacher=self.user)
#     def test_subject_get(self):
#         self.response = self.client.get(self.url)
#         self.assertEqual(self.response.status_code,200)
#
# class ScoreTest(TestCase):
#     def setUp(self):
#         self.url = reverse('scores')
#         self.user = User.objects.create_user(username='aliya',password='aliya.123456')
#         self.subject = Subject.objects.create(title='Биология', teacher=self.user)
#         Score.objects.create(subject=self.subject,pupil='Ученик',score=5,date_created=None)
#     def score_test_get(self):
#         self.response = self.client.get(self.url)
#         self.assertEqual(self.response.status_code,200)

