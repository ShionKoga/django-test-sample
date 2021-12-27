from django.test import TestCase, Client
from django.urls import reverse

class Tests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('store:meats')

    def test_meats(self):
        response = self.client.get(self.url)
        context = ['beaf', 'pork', 'chicken']
        self.assertEqual(response.status_code, 200, 'it returns status code 200')
        self.assertEqual(response.context['meats'], context, 'it returns correct context')
        self.assertTemplateUsed(response, 'meats.html', 'it uses correct template')
