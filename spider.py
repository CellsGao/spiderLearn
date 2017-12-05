import requests
import math

try:
    url = 'http://www.google.com/search?'
    kw = {'q': 'python'}
    r = requests.get(url, params=kw)
    r.raise_for_status()
    print(r.request.url)
    print(len(r.text))
    print(r.status_code)
except:
    print('error')
