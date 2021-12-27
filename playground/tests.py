from django.test import TestCase, Client
from django.urls import reverse

class Tests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('playground:hello')

    def test_hello(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200, 'it returns status code 200')
        self.assertEqual(response.context['name'], 'Mosh', 'it returns correct context')
        self.assertTemplateUsed(response, 'hello.html', 'it uses correct template')
