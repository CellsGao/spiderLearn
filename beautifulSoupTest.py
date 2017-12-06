import requests
from bs4 import BeautifulSoup

try:
    url = 'http://python123.io/ws/demo.html'
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    tag = soup.a
    para = soup.p
    # print(soup.text)
    print(tag.attrs['href'])
    print(type(tag.attrs))
    print(type(tag))
    print(para.string)
    print(type(para.string))
except:
    print('error')
