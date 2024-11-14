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

    def test_index_endpoint(self):
        response = self.client.get('/')
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Hello, World!')

    def test_create_user_success(self):
        payload = {'line_token': 'test_token'}
        response = self.client.post('/users', json=payload)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['line_token'], 'test_token')

    def test_create_user_no_data(self):
        payload = {}
        response = self.client.post('/users', json=payload)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'Data is required')
    

    

if __name__ == '__main__':
    unittest.main()

    