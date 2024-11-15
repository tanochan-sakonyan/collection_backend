import unittest
from unittest.mock import patch, MagicMock
from flask import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app

class UsersAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_create_user_success(self):
        payload = {'line_token': 'test_token'}
        response = self.client.post('/users', json=payload)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['line_token'], 'test_token')

    def test_register_paypay_url_success(self):
        payload = {'paypay_url': 'test_paypay_url'}
        response = self.client.post('/users/1/paypay-link', json=payload)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['paypay_url'], 'test_paypay_url')

    def test_register_paypay_url_no_data(self):
        payload = {}
        response = self.client.post('/users/100/paypay-link', json=payload)
        self.assertEqual(response.status_code, 400)

    
    

    

if __name__ == '__main__':
    unittest.main()

    