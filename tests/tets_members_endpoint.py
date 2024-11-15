import unittest
from unittest.mock import patch, MagicMock
from flask import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app
class EventsAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_create_member_success(self):
        payload = {'newMemberName': 'test_member'}
        response = self.client.post('/events/2/members', json=payload)
        
        # デバッグ用の出力
        print('Status Code:', response.status_code)
        print('Response Data:', response.data)
        print('Headers:', response.headers)
        
        data = response.get_json()
        self.assertIsNotNone(data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['member_name'], 'test_member')
        self.assertEqual(data['event_id'], 2)
    
    def test_create_member_no_data(self):
        payload = {}
        response = self.client.post('/events/2/members', json=payload)
        
        # デバッグ用の出力
        print('Status Code:', response.status_code)
        print('Response Data:', response.data)
        print('Headers:', response.headers)
        
        data = response.get_json()
        self.assertIsNotNone(data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['isSuccessful'], False)


if __name__ == '__main__':
    unittest.main()
