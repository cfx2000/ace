# coding:utf-8
import requests
from bs4 import BeautifulSoup
import os
# 创建一个文件夹名称
FileName = 'test'
if not os.path.exists(os.path.join(os.getcwd(), FileName)):     # 新建文件夹
     print(u'建了一个名字叫做', FileName, u'的文件夹！')
     os.mkdir(os.path.join(os.getcwd(),'test'))
else:
    print(u'名字叫做', FileName, u'的文件夹已经存在了！')
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"
}
url = 'https://item.jd.com/2145498.html'
response = requests.get(url, headers=headers)
html = requests.get(url).content    # 返回html
print(response.status_code)
soup  = BeautifulSoup(html,'html.parser')   # BeautifulSoup对象
print(soup.get_text)
price = soup.find('span', class_="p-price")#.find_all('img') # 找到图片信息
#jpg_data = soup.find_all('img', style="width: 650px;") # 找到图片信息
print(price)
# for i in price:
#     data = i['src'] # 图片的URL
#     print(data)
#     name = i['alt'] # 图片的名称
#     # if "https://www.dxsabc.com/" not in data:
#     #     data = 'http://www.xiaohuar.com'+data
#     r2 = requests.get(data)
#     fpath = os.path.join(FileName,name)
#     with open(fpath+'.jpg','wb+')as f : # 循环写入图片
#         f.write(r2.content)
#print('保存成功，快去查看图片吧！！')