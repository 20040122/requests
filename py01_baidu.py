import requests

resp=requests.get('http://www.baidu.com')
print(resp.text)