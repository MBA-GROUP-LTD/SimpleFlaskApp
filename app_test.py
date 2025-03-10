"""Unit test file fro app.py"""
import unittest
# from app import app
from app import returnRandomString

class SimpleFlaskAppTestCase(unittest.TestCase):
    # def setUp(self):
    #     self.app = app.test_client()
    #     self.app.testing = True

    def test_returnRandomString(self):
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'olleh')

        response = self.app.get('/world')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'dlrow')

        response = self.app.get('/12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), '54321')

        random_string = 'This is my test string'
        random_string_reversed = 'gnirts test ym si sihT'
        self.assertEqual(returnRandomString(random_string), random_string_reversed)

if __name__ == '__main__':
    unittest.main()