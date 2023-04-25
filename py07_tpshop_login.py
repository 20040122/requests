import requests
import unittest


def login():
    session = requests.Session()
    resp_l=session.get(url='http://127.0.0.1/index.php?m=Home&c=User&a=verify&r=0.8657985577446015')
    resp_v=session.post(url='http://127.0.0.1/index.php?m=Home&c=User&a=do_login&t=0.3509617992709504',
                        data={"username":"13555985732","password":"123456","verify_code":"8888"})
    return resp_v.json()

class TestTPShopLogin(unittest.TestCase):
    def test_login(self):
        resp=login()
        self.assertEqual('登陆成功',resp.get('msg'))