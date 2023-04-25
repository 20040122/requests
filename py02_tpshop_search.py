import requests

resp=requests.get(url='http://127.0.0.1/Home/Goods/search.html',params={'q':'iphone'})
print(resp.text)