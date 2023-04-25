import unittest
import requests

class TestihrmLogin(unittest.TestCase):
    def test_login(self):
        resp=requests.post(url='http://ihrm-java.itheima.net/api/sys/login',
                           headers={'Content-Type':'application/json'},
                           json={"mobile":"13800000002","password":123456})
        self.assertEqual(200,resp.status_code)
        self.assertEqual(True,resp.json().get('success'))
        self.assertEqual(10000,resp.json().get('code'))
        self.assertIn('操作成功',resp.json().get('message'))