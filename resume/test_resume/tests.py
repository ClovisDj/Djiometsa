from copy import deepcopy
import json
from django.test import TestCase
from django.test.client import Client
from resume.views import send_mail


class TestEmail(TestCase):
    def setUp(self):
        self.client = Client()
        # Bad email
        self.data_1 = {
            'name': 'clovis',
            'email': 'clovis@gmail',
            'subject': 'view testing',
            'message': 'Testing of ajax contact form.'
        }
        # Response for this set of data should be ok.
        self.data_2 = deepcopy(self.data_1)
        self.data_2['email'] = 'diclovis@gmail.com'

        # Missing field name
        self.data_3 = deepcopy(self.data_2)
        self.data_3['name'] = ''

    # Test bad email
    def test_data_1(self):
        response = self.client.post('/ajax/send_email/', self.data_1, HTTP_X_REQUESTED_WITH='XMLHttpRequest', enforce_csrf_checks=True)
        data = json.loads(response.content.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('Please verify', data['status'])

    # Test good data
    def test_data_2(self):
        response = self.client.post('/resume/ajax/send_email/', self.data_2, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        data = json.loads(response.content.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('good', data['status'])

    # Test empty field
    def test_data_3(self):
        response = self.client.post('/contact/ajax/send_email/', self.data_3, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        data = json.loads(response.content.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('Please verify', data['status'])

    # Test non ajax request
    def test_data_4(self):
        response = self.client.post('/ajax/send_email/', self.data_2)
        self.assertEqual(response.status_code, 400)
