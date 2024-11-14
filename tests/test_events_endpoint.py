import unittest
from flask import json
import sys
import os

# パスの設定はプロジェクト構成に応じて調整してください
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app

class EventsAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_create_event_success(self):
        payload = {'eventName': 'test_event', 'userId': 1}
        response = self.client.post('/events', json=payload)
        
        # デバッグ用の出力
        print('Status Code:', response.status_code)
        print('Response Data:', response.data)
        print('Headers:', response.headers)
        
        data = response.get_json()
        self.assertIsNotNone(data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['event_name'], 'test_event')
        self.assertEqual(data['user_id'], 1)

    def test_create_event_no_data(self):
        payload = {}
        response = self.client.post('/events', json=payload)
        
        # デバッグ用の出力
        print('Status Code:', response.status_code)
        print('Response Data:', response.data)
        print('Headers:', response.headers)
        
        data = response.get_json()
        self.assertIsNotNone(data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'Data is required')

if __name__ == '__main__':
    unittest.main()
