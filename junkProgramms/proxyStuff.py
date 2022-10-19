import requests 

header={'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
proxy='1.10.188.78:45208'
r=requests.get('https://httpbin.org/ip',headers=header,proxies={'https':proxy},timeout=10)
print(r.request.headers)
