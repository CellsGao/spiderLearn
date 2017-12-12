from bs4 import BeautifulSoup
import requests
import re

url = 'https://python123.io/ws/demo.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text, 'html.parser')
# for link in soup.find_all('a'):
#     print(link.get('href'))
# print(soup.find_all(['a', 'b']))  # 可以以列表形式查找多个标签
# for tag in soup.find_all(True):  # find_all(True)可以返回所有标签信息
#     print(tag.name)
# for tag in soup.find_all(re.compile('b')):
#     print(tag.name)
#print(soup.find_all('p', 'course'))
print(soup.find_all(id=re.compile('link')))
print(soup(id=re.compile('link')))  # 与soup.find_all()等效
