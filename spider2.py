import os
import requests

url = 'http://image.nationalgeographic.com.cn/2017/1205/20171205022846699.jpg'
root = '/Users/gaoshang/Downloads/pics/'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
        r = requests.get(url)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
        print('success 1')
    elif os.path.exists(root):
        r = requests.get(url)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
        print('success 2')
except:
    print("error")


