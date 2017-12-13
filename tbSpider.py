import requests
import re

def getHtmlText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('getHtmlText函数出现错误')

def parseHtml(list,html):
    try:
        tlt=re.findall(r'\"raw_title\":\".*？\"',html)
        plt=re.findall(r'\"view_price\":\"[1-9]\d*.\d*|0.\d*[1-9]\d*\"',html)
        for i in len(plt):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            list.append([price,title])
    except:
        print('parseHtml函数出现错误')



def printList(list):
    print('')

def main():
    try:
        start_url = 'https://s.taobao.com/search?q='
        goods = input('请输入要搜索的物品')
        depth = input('请输入要搜索的页面数')
        list=[]
        for i in range(int(depth)):
            text = getHtmlText(start_url + goods + '&s=' + str(44 * int(depth)))
            parseHtml(list, text)
    except ValueError:
        print('输入数据类型错误')
    printList(list)

if __name__ == '__main__':
    main()