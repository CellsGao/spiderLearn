from bs4 import BeautifulSoup
import requests

try:
    url = 'https://python123.io/ws/demo.html'
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup.a.next_sibling)  # 'and'  HTML中标签外的文字也算标签
    # print(soup.a.next_sibling.next_sibling)  # <a>...</a>
    for sibling in soup.a.next_siblings:
        if sibling is None:
            break
        else:
            print(sibling.name)  # 'and'字符串的sibling.name返回none

    print(soup.prettify())
    print(soup.a.prettify())
except:
    print('error')
    print(r.status_code)
