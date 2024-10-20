from datetime import timezone

from django.test import TestCase
from django.urls import reverse

from polls.models import Question


class PollsViewsTests(TestCase):
    def test_index_view_status_code(self):
        url = reverse('polls:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_view_status_code(self):
        question = Question.objects.create(question_text="Sample question?", pub_date=timezone.now())
        url = reverse('polls:detail', args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_404_on_invalid_question(self):
        url = reverse('polls:detail', args=(9999,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
