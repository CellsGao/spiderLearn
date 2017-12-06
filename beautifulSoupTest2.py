from bs4 import BeautifulSoup
import requests

try:
    url = 'https://python123.io/ws/demo.html'
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup.head)
    # print(soup.head.contents)
    # print(soup.body)
    # print(soup.body.contents)
    # print(len(soup.body.contents))
    # print(type(soup.body.contents))  # list
    # print(type(soup.body))   #bs4.element.tag
    # for child in soup.body.children:
    #     print(child)
    print(type(soup.a.parents))  # generator
    for parent in soup.a.parents:
        if parent is None:
            break
        else:
            print(parent.name)
except:
    print('error')
    print(r.status_code)
