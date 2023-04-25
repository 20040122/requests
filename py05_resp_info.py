import requests

resp=requests.get(url='http://www.baidu.com')

print(resp.url)
print(resp.status_code)
print(resp.cookies)