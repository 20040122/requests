import requests

resp=requests.post(url='http://127.0.0.1/index.php?m=Home&c=User&a=do_login&t=0.013691649986960153',
                   headers={"Content-Type":"text/html"},
                   data={"username":"13800138006","password":"123456","verify_code":"8888"})
print(resp.json())