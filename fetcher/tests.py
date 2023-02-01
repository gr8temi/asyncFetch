from django.test import Client, TestCase
import json


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn("quotes", content)
        self.assertIn("user", content)
