import requests

resp=requests.post(url='http://ihrm-java.itheima.net/api/sys/login',
                   headers={'Content-Type':'application/json'},
                   json={"mobile":"13800000002","password":123456})
print(resp.json())