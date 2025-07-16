from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class SimpleTestCase(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_contact_form_submission(self):
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'This is a test message.'
        }

        response = self.client.post(reverse('home'), data)
        self.assertEqual(response.status_code, 200)