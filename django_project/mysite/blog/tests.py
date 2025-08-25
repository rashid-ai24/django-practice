from django.test import TestCase
from django.urls import reverse

class BlogTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse("blog-home"))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(reverse("blog-about"))
        self.assertEqual(response.status_code, 200)
