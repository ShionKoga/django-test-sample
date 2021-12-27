from django.test import TestCase, Client
from django.urls import reverse

class Tests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('texts:alphabets')

    def test_alphabets(self):
        response = self.client.get(self.url)
        context = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        self.assertEqual(response.status_code, 200, 'it returns status code 200')
        self.assertEqual(response.context['alphabets'], context, 'it returns correct context')
        self.assertTemplateUsed(response, 'alphabets.html', 'it uses correct template')
