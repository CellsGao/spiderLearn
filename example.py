from bs4 import BeautifulSoup
import requests
import re
import bs4


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        print('error')
        return ''


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all('td')
            ulist.append([tds[0].next, tds[1].string, tds[3].string])


def printUnivList(ulist, num):
    tplt = '{0:10}\t{1:{3}^10}\t{2:^6}'
    print(tplt.format("排名", "学校名称", "总分",chr(12288)))  # 数字表宽度
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2017.html'
    html = getHtmlText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)


main()
